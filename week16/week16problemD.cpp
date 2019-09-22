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
  std::cin >> n;
  set <int, greater <int> > nums;
  for (int i = 0; i < n; i++) {
    int cur;
    std::cin >> cur;
    nums.insert(cur);
  }
  if (nums.find(0) != nums.end())
    nums.erase(0);
  std::cout << nums.size() << "\n";
  return 0;
}
