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
  string letters;
  std::cin >> letters;
  int qs = 0;
  for (int i = 0; i < letters.length(); i++) {
    if (letters[i] == 'Q')
      qs += 1;
  }
  int totalqaq = 0;
  int curqs = 0;
  for (int i = 0; i < letters.length(); i++) {
    if (letters[i] == 'Q')
      curqs += 1;
    if (letters[i] == 'A')
      totalqaq += curqs*(qs-curqs);
  }
  std::cout << totalqaq << "\n";
  return 0;
}
