#include <cstring>
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
  int t;
  std::cin >> t;
  for (int i = 0; i < t; i++) {
    int n;
    std::cin >> n;
    string s;
    std::cin >> s;
    bool possible = true;
    for (int j = 0; j < n/2 + 1; j++) {
      int difference = abs(s[j]-s[n-j-1]);
      if ((difference != 0) and (difference != 2))
	  possible = false;
    }
    if (possible)
      std::cout << "YES\n";
    else
      std::cout << "NO\n";
  }
  return 0;
}
