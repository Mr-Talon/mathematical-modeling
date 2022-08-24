#pragma once

class CNC
{
private:
	int number;   //CNC编号
	int position; //CNC位置
	int knife;    //CNC刀具型号,1第一道工序，2第二道工序
	int count;    //CNC剩余工作时间
	int n;        //加工物序列号
public:
	CNC();
	CNC(int num, int pos, int kni);
	void countdown(int temp);
	friend class RGV;
};
