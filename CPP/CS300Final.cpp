#include <iostream>
#include <time.h>
#include <algorithm>
#include <Parser.cvs>

using namespace std;

int main{
//Set up a way to store course information
struct Course {
    string coursenum;// hold the course number
    string coursename; // hold the course name
    string prerequisite; // tell is there is any prereuisites
};

// how to display courses
void displayCourse(Course course){
    cout << course.coursenum << ": " << course.coursename<< ": "<< course.prerequisite<< endl;
    return;
}

// Gather information for the courses from the users
Course getCourse(){
    Course course;
    cout << "Enter course number: "; // get course number
    cin.ignore();
    getline(cin,course.coursename);
    cout << "Enter course name: "; // get course name
    cin.ignore();
    getline(cin,course.prerequisite);
    cout << "Enter course prerequisite: ";  //get any prerequisites required
    cin.ignore();
    getline(cin,course.prerequisite);
    return course;
}
//Make a vector to get the cvs information
// information found on gormanalysis.com
Vector <Course> loadCourses(string Parser-sheet1.cvs) {
    cout << "Loading Course Information" <<Parser-sheet1.cvs << endl;
    vector <Course> course; // hold the course information
    csv::Parser file = cvs::Parser(cvsPath);
    
    try{
        //make a loop to get all of the information from the cvs file
        // information found on gormanalysis.com
        for (int i = 0; i < Parser.rowCount(); i++){
            Course course;
            course.coursenum    = file [i][1];
            course.coursename = file[i][0];
            course.prerequisite = file [i] [2];
            course.push_Back(course);
        }
        catch (csv::Error &e) {
            std::cerr << e.what() << std::endl;
        }
    }
    return courses;

}
// information to use a quick sort from geeksforgeeks.org
// sort the course name first
int partition(vector <Course> & course, int begin, int end) {
    int low = begin;
    int high = end;
// make a pivot point
    int pivot = begin + (end - begin)/2;
    bool done = false;
    while (!done){
        //Sort from the low end and increase up
        while (Course.at(low).coursename.compare(course.at(high).coursename)<0){
            ++low;
        }
        //Sort for the high end and decrease down
        while (course.at(pivot).coursename.compare(course.at(high).coursename)<0){
            --high;
        }
        if (low >= high){
            finished = true;
        }
        else {
            swap(course.at(low), bids.at(high));
        }
                
    }
    return high;
}
//run the quicksort function  for course names
void quickSort(vector<Course>& course, int begin, int end){
    int mid = 0;
    // check to see if there is 1 or less courses to sort
    if (begin >= end){
        return;
    }
    //sort list from smallest to middle
    mid = partition(course, begin, end);
    quickSort(course,begin,end);

    // sort list from middle to high end
    quickSort(cours, mid+1, end);
    }
//Set up for the user entered information
// information from docs.microsoft.com
int main(int argc, char* argv[]){
    string parser;
    switch (argc) {
        case 2:
        parser = argv[1];
        break;
    default:
        Parser"userInput"
    }
    // make a vector to hold the user input
    vector<Courses> userInput;
 // make the menu for selection options.
    int choice = 0;
        while (choice !=4){
            cout << "Menu: " << endl;
            cout << "1. Load Data Structure: " << endl;
            cout << "2. Print Course LIst: " << endl;
            cout << "3. Print Course: " << endl;
            cout << "4. Exit" << endl;
            cout << "Enter your choice: ";
            cin >> choice;

    return 0;
}