#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <stdio.h>
#include <cstdlib>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

using namespace std;

void truncate_error(char *filename);

void decode(char* filename);


int main()
{
	string day, num, line, temp, instr;
    ifstream fin;
    char* call;
    char fname[] = {"temp.gz"};

	for (int x = 1; x < 31; x++)
	{
        stringstream ss;
        ss << x;

		if (x < 10)
		{
			num = ss.str();
			day = "0" + num;
		}
		else
		{
			day = ss.str();
		}

        fin.open("iPlane_traces/" + day + "/traces.txt");

        while (getline(fin, temp))
        {
        	instr = "wget http://iplane.cs.washington.edu/data/iplane_logs/2016/04/01/" + temp + " -O temp.gz";
        	system(instr.c_str());
        	system("gzip -dc temp.gz > temp.out");
        	system("./a.out temp.out > temp.txt");
        	system("python iplane.py");
        }

        fin.close();
	}

	return 0;
}