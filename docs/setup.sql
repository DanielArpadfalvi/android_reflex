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
  token uuid,
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

create or replace function get_board(pw text, tok text default null, who text default null)
returns jsonb language plpgsql security definer set search_path = public as $$
declare
  is_admin boolean := check_admin(pw);
  my_name text;
  unlocked boolean;
begin
  if not check_password(pw) and not is_admin then
    raise exception 'Hibás jelszó';
  end if;
  -- a többiek tippjei csak a saját tipp leadása után (token vagy név), szülőnek, vagy születés után láthatók
  select name into my_name from tips where tok is not null and token::text = tok;
  if my_name is null and who is not null then
    select name into my_name from tips where name_key = lower(trim(who));
  end if;
  unlocked := is_admin or my_name is not null or exists (select 1 from result where id = 1);
  return jsonb_build_object(
    'locked', not unlocked,
    'count', (select count(*) from tips),
    'my_name', my_name,
    'tips', case when unlocked then coalesce((select jsonb_agg(jsonb_build_object('name', name, 'data', data) order by updated_at) from tips), '[]'::jsonb) else '[]'::jsonb end,
    'result', (select data from result where id = 1)
  );
end $$;

create or replace function submit_tip(pw text, tip_name text, tip jsonb, tok text default null)
returns text language plpgsql security definer set search_path = public as $$
declare
  k text := lower(trim(tip_name));
  existing tips%rowtype;
  new_tok uuid;
begin
  if not check_password(pw) then raise exception 'Hibás jelszó'; end if;
  if exists (select 1 from result where id = 1) then
    raise exception 'Bence már megszületett, a tippelés lezárult';
  end if;
  if length(trim(tip_name)) = 0 or length(tip_name) > 60 then
    raise exception 'Érvénytelen név';
  end if;
  select * into existing from tips where name_key = k;
  if found then
    if existing.token is not null and (tok is null or existing.token::text <> tok) then
      raise exception 'Ezen a néven már van tipp. Ha a tiéd, azt csak abból a böngészőből módosíthatod, ahonnan leadtad. Ha nem a tiéd, válassz másik nevet!';
    end if;
    new_tok := coalesce(existing.token, gen_random_uuid());
    update tips set name = trim(tip_name), data = tip, token = new_tok, updated_at = now() where name_key = k;
  else
    -- ha ugyanaz a böngésző más névvel tippel újra, a régi tippje átnevezésre kerül
    if tok is not null and exists (select 1 from tips where token::text = tok) then
      update tips set name_key = k, name = trim(tip_name), data = tip, updated_at = now() where token::text = tok
      returning token into new_tok;
    else
      new_tok := gen_random_uuid();
      insert into tips (name_key, name, data, token, updated_at) values (k, trim(tip_name), tip, new_tok, now());
    end if;
  end if;
  return new_tok::text;
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

revoke all on function check_password(text), check_admin(text), get_board(text, text, text),
  submit_tip(text, text, jsonb, text), set_result(text, jsonb), delete_tip(text, text) from public;
grant execute on function check_password(text), check_admin(text), get_board(text, text, text),
  submit_tip(text, text, jsonb, text), set_result(text, jsonb), delete_tip(text, text) to anon, authenticated;
