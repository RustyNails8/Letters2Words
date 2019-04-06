#include <string>
#include <iostream>
#include <fstream>
using namespace std;


/*void writeToFile(ofstream &outputFile, string x)
{
    outputFile << x << endl;
}
*/

void get( string str, string res ) {

   cout << res << endl;

   for( int i = 0; i < str.length(); i++ )
      get( string(str).erase(i,1), res + str[i] );
}

int main( int argc, char **argv) {

    // string str = "wtehi" ;
    string myWORD ;
    // cout << "Enter your String:   ... " ;
    // cin >> myword ;
	myWORD = argv[1] ;
   	get( myWORD, "" ) ;

   	return 0;
}


// https://stackoverflow.com/questions/29059461/algorithm-to-print-all-combination-of-letters-of-the-given-string-in-lexicograph
