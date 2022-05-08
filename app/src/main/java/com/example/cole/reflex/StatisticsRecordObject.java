package com.example.cole.reflex;

import java.util.ArrayList;


public class StatisticsRecordObject {

    private ArrayList<SingleStatistics> singleStatsArray = new ArrayList<SingleStatistics>();
    private int[] twoPlayerMode = new int[2];
    private int[] threePlayerMode = new int[3];
    private int[] fourPlayerMode =new int[4];

    public static void createStatisticsObject(){
    }


    /** Now I am going to provide a TON of methods to access these values stored within
     * this object...
     **/

    public ArrayList<SingleStatistics> getSingleStatsArray() {
        return singleStatsArray;
    }

    public int[] getTwoPlayerMode() {
        return twoPlayerMode;
    }

    public int[] getThreePlayerMode() {
        return threePlayerMode;
    }

    public int[] getFourPlayerMode() {
        return fourPlayerMode;
    }


    public void addSingleStat(SingleStatistics singleStatisticsObject){
        singleStatsArray.add(singleStatisticsObject);
    }

    public void addTwoPlayerPlayerOne(){

    }
}
