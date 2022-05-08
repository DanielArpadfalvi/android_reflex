package com.example.cole.reflex;

public class StatisticsObject{
    private long nanoSecondsValue;
    private long millisecondsValue = nanoSecondsValue/1000000;


    public long getMillisecondsValue() {
        return millisecondsValue;
    }


    public StatisticsObject(long nanoSecondsValue) {
        this.nanoSecondsValue = nanoSecondsValue;
    }

    public long getNanoSecondsValue() {
        return nanoSecondsValue;
    }

    public void setNanoSecondsValue(long nanoSecondsValue) {
        this.nanoSecondsValue = nanoSecondsValue;
    }

    public StatisticsObject(){}

    @Override
    public String toString() { return Long.toString(this.getNanoSecondsValue()); }

}
