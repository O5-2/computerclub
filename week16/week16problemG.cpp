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
  int n;
  std::cin >> n;
  set <char, greater <char> > chars;
  for (int i = 0; i < n; i++) {
    char cur;
    std::cin >> cur;
    chars.insert(cur);
  }
  if (n >= 27)
    std::cout << "-1\n";
  else
    std::cout << n-chars.size() << "\n";
  return 0;
}
