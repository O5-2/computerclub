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

using namespace std;

int main()
{
  ios::sync_with_stdio(false);
  std::cin.tie(0);
  int n;
  int m;
  std::cin >> n >> m;
  string s;
  std::cin >> s;
  int l;
  int r;
  char cA;
  char cB;
  string cur;
  for (int i = 0; i < m; i++) {
    std::cin >> l >> r >> cA >> cB;
    cur = s.substr(0, max(0, l-1));
    for (int j = l-1; j < r; j++) {
      if (s[j] == cA)
	cur += cB;
      else
	cur += s[j];
    }
    if (r < s.size())
      cur += s.substr(r);
    s = cur;
  }
  std::cout << s << "\n";
  return 0;
}
