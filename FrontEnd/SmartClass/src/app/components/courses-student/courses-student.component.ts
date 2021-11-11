import { Component, OnInit } from '@angular/core';
import {RestService} from "../../services/rest.service";

@Component({
  selector: 'app-courses-student',
  templateUrl: './courses-student.component.html',
  styleUrls: ['./courses-student.component.css']
})
export class CoursesStudentComponent implements OnInit {
  messageOk = null;
  messageError = null;
  request = {
    tipo: 4,
    carnet: localStorage.getItem("carnet"),
    year: "",
    semestre: ""
  }
  constructor(private rest: RestService) { }

  ngOnInit(): void {
  }

  async getReport(){
    try {
      var response = await this.rest.PostRequest("reportCourseStd", this.request).toPromise()
      this.messageOk = response.message;
    }catch (e) {
      this.messageError = e.error.message;
    }
  }

  closeAlert1(){
    this.messageOk = null;
  }

  closeAlert2(){
    this.messageError = null;
  }
}
