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
  int num = 0;
  for (int a = 1; a < n+1; a++) {
    for (int b = a+0; b < n+1; b++) {
      int c = a ^ b;
      if (((b <= c) and (c <= n)) and (a+b > c))
	num += 1;
    }
  }
  std::cout << num << "\n";
  return 0;
}
