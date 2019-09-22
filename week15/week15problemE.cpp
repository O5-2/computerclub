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
  int squareroot = ceil(sqrt(n))+1;
  int factors[squareroot];
  int ways = 1;
  for (int i = 2; i < squareroot; i++) {
    factors[i] = 0;
    while (n % i == 0) {
      n /= i;
      factors[i] += 1;
    }
    ways *= factors[i]+1;
  }
  if (n != 1)
    ways *= 2;
  ways -= 1;
  std::cout << ways << "\n";
  return 0;
}
