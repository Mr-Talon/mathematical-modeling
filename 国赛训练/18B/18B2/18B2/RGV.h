#pragma once
#include "CNC.h"
using namespace std;
class RGV
{
private:
	int position;	//rgv当前位置
	int now_cnc;	//rgv当前CNC对象
	int rgv_flag;	//RGV当前状态，1空闲，2持有半成品
	int rgv_n;		//RGV当前半成品号
public:
	int time; //总用时
	int sum; //加工熟料总数

	RGV();
	int find(CNC* p); //寻找最优解
	void Init(CNC* p); //第一轮初始化
	int posCalculate(int pos1, int pos2); //计算RGV移动时间
	void move(CNC* p); //RGV移动
	void load(CNC* p); //RGV上下料
	void wait(CNC* p);//RGV等待
};
