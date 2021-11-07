import { Component, OnInit } from '@angular/core';
import {RestService} from "../../services/rest.service";

@Component({
  selector: 'app-liststudents-admin',
  templateUrl: './liststudents-admin.component.html',
  styleUrls: ['./liststudents-admin.component.css']
})
export class ListstudentsAdminComponent implements OnInit {
  listStudents: any[] = [];
  selectedStudent = {
    carnet: "",
    dpi: "",
    name: "",
    degree: "",
    email: "",
    password: "",
    age: ""
  }
  messageOk = null
  messageError = null
  request = {
    "type": "",
    "key": ""
  }

  constructor(private rest: RestService) { }

  ngOnInit(): void {
  }

  async getListStudent(){
    try {
      var response = await this.rest.GetRequest("/listStudents/"+this.request.type+"/"+this.request.key).toPromise();
      this.listStudents = response.listStudents;
      this.request.key = "";
      this.request.type = "";
      this.messageOk = response.message;
    }catch (e) {
      this.messageError = e.error.message;
    }
  }

  dataCrypted(type:string){
    this.request.type = type;
    this.getListStudent();
  }

  dataDeCrypted(type:string){
    this.request.type = type;
    this.getListStudent();
  }

  viewStudent(student:any){
    this.selectedStudent = student;
  }
}
