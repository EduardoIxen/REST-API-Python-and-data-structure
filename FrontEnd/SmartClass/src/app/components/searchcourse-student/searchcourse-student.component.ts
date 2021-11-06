import { Component, OnInit } from '@angular/core';
import {RestService} from "../../services/rest.service";

@Component({
  selector: 'app-searchcourse-student',
  templateUrl: './searchcourse-student.component.html',
  styleUrls: ['./searchcourse-student.component.css']
})
export class SearchcourseStudentComponent implements OnInit {
  codeCourse = 0
  constructor(private rest: RestService) { }

  ngOnInit(): void {
  }

  async searchCourse(){
    try {
      var response = await this.rest.GetRequest("/searchCourse/"+this.codeCourse).toPromise();
      this.codeCourse = 0;
    }catch (e) {
      console.log(e.error.message);
    }
  }

}
