#pragma once
#include "CNC.h"
class RGV
{
private:
	int position; //rgv当前位置
	int now_cnc;   //当前目标
	int rgv_flag;  //rgv_flag,1有熟料,0无

public:
	int time; //总用时
	int sum; //加工熟料总数

	RGV();
	void Init(CNC* p); //第一轮初始化
	int posCalculate(int pos1, int pos2); //计算RGV移动时间
	void move(CNC* p); //RGV移动
	void load(CNC* p); //RGV上下料
	void clean(CNC* p);//RGV清洗
	void wait(CNC* p);//RGV等待
};
