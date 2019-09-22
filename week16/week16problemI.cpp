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
  string s;
  std::cin >> s;
  string t;
  std::cin >> t;
  int i = 0;
  while (((i < s.length()) and (i < t.length())) and (s[s.length()-i-1] == t[t.length()-i-1])) {
    i += 1;
  }
  std::cout << s.length()+t.length()-(2*i) << "\n";
  return 0;
}
