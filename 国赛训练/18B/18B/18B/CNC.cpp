#include "stdafx.h"
#include "CNC.h"
using namespace std;
CNC::CNC(int num, int pos)
{
	number = (num > 0) ? num : ERROR;
	position = (pos >= 0) ? pos : ERROR;
	count = 0;
	n = 0;
}


void CNC::countdown(int temp)
{
	if (count > temp) {
		count -= temp;
	}
	else {
		count = 0;
	}
}
