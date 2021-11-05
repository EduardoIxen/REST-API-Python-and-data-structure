import { Component, OnInit } from '@angular/core';
import {RestService} from "../../services/rest.service";

@Component({
  selector: 'app-notes-student',
  templateUrl: './notes-student.component.html',
  styleUrls: ['./notes-student.component.css']
})
export class NotesStudentComponent implements OnInit {
  note = {
    carnet: "",
    title: "",
    content: ""
  }
  messageOk = null
  messageError = null

  arrayPr: any[] = [];

  selectedNote = {
    title: "",
    content: ""
  }

  constructor(private rest: RestService) { }

  ngOnInit(): void {
    this.getListNotes();
  }

  async newNote(){
    try {
      // @ts-ignore
      this.note.carnet = localStorage.getItem("carnet");
      //this.note.carnet = this.rest.getUserLogged().carnet;
      var response = await this.rest.PostRequest("newNote", this.note).toPromise();
      var response2 = await this.rest.GetRequest("reportHash").toPromise();
      this.note.title = "";
      this.note.content = "";
      this.messageOk = response.message;
      this.getListNotes();
    }catch (e:any) {
      this.messageError = e.error.message;
    }
  }

  async getListNotes(){
    // @ts-ignore
    var id_student = localStorage.getItem("carnet");
    console.log(id_student);
    var response = await this.rest.GetRequest(`/notesStudent/`+id_student).toPromise();
    this.arrayPr = response.listNotes;
    console.log(response);
  }

  viewNote(note:any){
    this.selectedNote = note;
  }

  closeAlert1(){
    this.messageOk = null;
  }

  closeAlert2(){
    this.messageError = null;
  }
}
