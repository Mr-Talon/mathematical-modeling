#include "stdafx.h"
#include "RGV.h"
#include "CNC.h"

#define CNCNUMBER 8
#define TIME 28800
using namespace std;
int main()
{
	RGV rgv;   //创建RGV对象
	CNC cnc[CNCNUMBER] = {   // 创建CNC对象数组
		CNC(1,0), CNC(2,0), CNC(3,1), CNC(4,1),
		CNC(5,2), CNC(6,2), CNC(7,3), CNC(8,3) };
	CNC* pCNC = cnc;  //CNC数组指针

	cout << "时间" << '\t' << "下料开始" << '\t' << "上料开始" << '\t' << "CNC#" << endl;

	/*第一轮
	仅需考虑RGV“移动”和“上下料”动作*/
	rgv.Init(pCNC);

	/*第(n+1)轮
	RGV循环“移动”，“上下料”和“清洗”动作*/
	while (rgv.time <= TIME)
	{
		rgv.move(pCNC);
		rgv.load(pCNC);
		rgv.clean(pCNC);
	}
	cout << "生成熟料总数：" << rgv.sum << endl;
	system("pause");
	return 0;
}
