#include <iostream>
#include <fstream>
using namespace std;

void writeToFile(ofstream &outputFile, int x)
{
    outputFile << x << endl;
}

int main()
{
    ofstream outputFile;
    outputFile.open("program3data.txt");
    for (int i = 0; i < 10; i++)
    {
        writeToFile(outputFile, i);
    }
    outputFile.close();
    return 0;
}