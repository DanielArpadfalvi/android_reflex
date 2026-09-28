-- Bence tippjáték – Supabase adatbázis beállítás
-- Futtasd le egyszer a Supabase SQL Editorban.
-- A két jelszót ÁLLÍTSD ÁT lent (családi jelszó + szülői/admin jelszó)!

create table if not exists settings (
  key text primary key,
  value text not null
);

create table if not exists tips (
  name_key text primary key,
  name text not null,
  data jsonb not null,
  updated_at timestamptz not null default now()
);

create table if not exists result (
  id int primary key default 1 check (id = 1),
  data jsonb not null,
  updated_at timestamptz not null default now()
);

-- RLS bekapcsolva, policy nélkül: a táblák közvetlenül nem olvashatók/írhatók,
-- csak az alábbi jelszóval védett függvényeken keresztül.
alter table settings enable row level security;
alter table tips enable row level security;
alter table result enable row level security;

insert into settings (key, value) values
  ('family_password', 'CSALADI_JELSZO'),
  ('admin_password',  'SZULOI_JELSZO')
on conflict (key) do update set value = excluded.value;

create or replace function check_password(pw text)
returns boolean language sql security definer set search_path = public as $$
  select exists (select 1 from settings where key = 'family_password' and value = pw);
$$;

create or replace function check_admin(pw text)
returns boolean language sql security definer set search_path = public as $$
  select exists (select 1 from settings where key = 'admin_password' and value = pw);
$$;

create or replace function get_board(pw text)
returns jsonb language plpgsql security definer set search_path = public as $$
begin
  if not check_password(pw) and not check_admin(pw) then
    raise exception 'Hibás jelszó';
  end if;
  return jsonb_build_object(
    'tips', coalesce((select jsonb_agg(jsonb_build_object('name', name, 'data', data) order by updated_at) from tips), '[]'::jsonb),
    'result', (select data from result where id = 1)
  );
end $$;

create or replace function submit_tip(pw text, tip_name text, tip jsonb)
returns void language plpgsql security definer set search_path = public as $$
begin
  if not check_password(pw) then raise exception 'Hibás jelszó'; end if;
  if exists (select 1 from result where id = 1) then
    raise exception 'Bence már megszületett, a tippelés lezárult';
  end if;
  if length(trim(tip_name)) = 0 or length(tip_name) > 60 then
    raise exception 'Érvénytelen név';
  end if;
  insert into tips (name_key, name, data, updated_at)
  values (lower(trim(tip_name)), trim(tip_name), tip, now())
  on conflict (name_key) do update set name = excluded.name, data = excluded.data, updated_at = now();
end $$;

create or replace function set_result(pw text, res jsonb)
returns void language plpgsql security definer set search_path = public as $$
begin
  if not check_admin(pw) then raise exception 'Hibás szülői jelszó'; end if;
  if res is null then
    delete from result where id = 1;
  else
    insert into result (id, data, updated_at) values (1, res, now())
    on conflict (id) do update set data = excluded.data, updated_at = now();
  end if;
end $$;

create or replace function delete_tip(pw text, tip_name text)
returns void language plpgsql security definer set search_path = public as $$
begin
  if not check_admin(pw) then raise exception 'Hibás szülői jelszó'; end if;
  delete from tips where name_key = lower(trim(tip_name));
end $$;

revoke all on function check_password(text), check_admin(text), get_board(text),
  submit_tip(text, text, jsonb), set_result(text, jsonb), delete_tip(text, text) from public;
grant execute on function check_password(text), check_admin(text), get_board(text),
  submit_tip(text, text, jsonb), set_result(text, jsonb), delete_tip(text, text) to anon, authenticated;
