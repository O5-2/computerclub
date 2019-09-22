#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>

#include <cmath>
#include <iomanip>

using namespace std;

int main()
{
  ios::sync_with_stdio(false);
  std::cin.tie(0);
  string s;
  std::cin >> s;
  int len = s.length();
  while (len > 0) {
    bool possible = true;
    for (int i = 0; i < s.length()-len+1; i++) {
      string forwards = s.substr(i, len); 
      string backwards = forwards+"";
      reverse(backwards.begin(), backwards.end());
      if (forwards != backwards) {
	possible = false;
	break;
      }
    }
    if (possible)
      len -= 1;
    else
      break;
  }
  std::cout << len << "\n";
  return 0;
}
