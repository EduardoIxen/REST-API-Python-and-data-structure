import { Component, OnInit } from '@angular/core';
import {RestService} from "../../services/rest.service";

@Component({
  selector: 'app-homeadmin',
  templateUrl: './homeadmin.component.html',
  styleUrls: ['./homeadmin.component.css']
})
export class HomeadminComponent implements OnInit {
  messageError = null
  messageOk = null
  constructor(private rest:RestService) { }

  ngOnInit(): void {
  }

  async getTree(){
    try{
      var response = await this.rest.GetRequest("merkleStd").toPromise()
      this.messageOk = response.message;
    }catch (e) {
      this.messageError = e.error.message;
    }
  }

  async getTreeNotes(){
    try{
      var response = await this.rest.GetRequest("merkleNotes").toPromise()
      this.messageOk = response.message;
    }catch (e) {
      this.messageError = e.error.message;
    }
  }

  async getTreeCourses(){
    try{
      var response = await this.rest.GetRequest("merkleCourses").toPromise()
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
