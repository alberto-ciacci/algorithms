#include <iostream>
#include <vector>
#include <math.h> 
#include <iomanip>
#include <stdlib.h>

using namespace std;

int travel_refills(int total_distance, int tank_capacity, vector<int> & stops){
	int covered_segment;
	int position = 0;
	int n_refills = 0;
	int n = stops.size();
	while(position < total_distance){
		
		 int furthest_station_idx = 0;
		 int flag = 0;
		 for(int j = 0; j < n; ++j){
		     if((stops[j] > position) & (tank_capacity - (stops[j] - position) >= 0)){
		     	 flag = 1;
		     	 furthest_station_idx = j;
			 }
	     }
	     if (position + tank_capacity >= total_distance){
	     	 return n_refills;
		 }
	     if (flag == 0){
	     	 return -1;
		 }
		 covered_segment = (stops[furthest_station_idx] - position);
		 position += covered_segment;
		 n_refills += 1;
	}
}

int main() {
  int distance;
  int tank_capacity;
  int n;
  cout << "Input the distance that the vehicle must cover (integer): ";
  cin >> distance ;
  cout << "Input the capacity of the vehicle tank (integer): ";
  cin >> tank_capacity;
  cout << "Input the number of gas stations between the starting and the ending point of the route (integer): ";
  cin >> n;
  vector<int> stops(n);
  if (n > 0){
		  cout << "Input the positions of the gas stations in the route (0 < position < distance to be covered): " << "\n";
		  for (int i = 0; i < n; i++) {
		  	  cout << "Position #" << i + 1 << ": ";
		      cin >> stops[i];
		      if((stops[i] <= 0) | (stops[i] >= distance)){
		      	   cout << "Wrong input, the program is now closing.";
		      	   exit(0);
			  }
		  }
  }
  int n_refills = travel_refills(distance, tank_capacity, stops);
  if (n_refills >= 0){
  	  cout << "A distance of " << distance << " miles has been covered with " << n_refills << " refills of the vehicle tank.";
  }else{
  	  cout << "It was not possible to reach the destination. The vehicle ran out of fuel in the middle of the route.";
  }
}
