#pragma once
class CNC
{
private:
	int number;   //CNC编号   1-8
	int position; //CNC位置     0-3
	int count;    //CNC剩余工作时间
	int n;        //加工物序列号
public:
	CNC(int num, int pos);
	void countdown(int tem);
	friend class RGV;
};
