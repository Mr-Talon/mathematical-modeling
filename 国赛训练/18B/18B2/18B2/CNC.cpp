#include "stdafx.h"
#include "CNC.h"
CNC::CNC() {

}
CNC::CNC(int num, int pos, int kni)
{
	number = (num > 0) ? num : ERROR;
	position = (pos >= 0) ? pos : ERROR;
	knife = (kni == 1 || kni == 2) ? kni : ERROR;
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
