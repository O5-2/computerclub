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

using namespace std;

int main()
{
  ios::sync_with_stdio(false);
  std::cin.tie(0);
  int n;
  std::cin >> n;
  int likes[n];
  for (int i = 0; i < n; i++) {
    std::cin >> likes[i];
  }
  bool triangle = false;
  for (int i = 0; i < n; i++) {
    if (likes[likes[likes[i]-1]-1]-1 == i) {
      triangle = true;
      break;
    }
  }
  if (triangle)
    std::cout << "YES\n";
  else
    std::cout << "NO\n";
  return 0;
}
