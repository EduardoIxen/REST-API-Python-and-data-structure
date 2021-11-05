import { Component, OnInit } from '@angular/core';
import {RestService} from "../../services/rest.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-loadfile',
  templateUrl: './loadfile.component.html',
  styleUrls: ['./loadfile.component.css']
})
export class LoadfileComponent implements OnInit {
  private listTypeLoad = [
    {
      id:1,
      content:"Carga masiva de estudiantes"
    },
    {
      id: 2,
      content: "Carga masiva de cursos de pensum"
    },
    {
      id:3,
      content:"Carga masiva de cursos del estudiantes"
    },
    {
      id:4,
      content:"Carga masiva de los apuntes de estudiantes"
    }
  ];
  idSelectedType = 0;
  selected = {}
  pathFile: any = null
  messageOk = null
  messageError = null
  objectSend = {
    tipo:"",
    contenido:"",
    path:"",
    Cursos:""
  }

  constructor(private rest: RestService, private route: Router) { }

  ngOnInit(): void {
  }

  getListTypeLoad(): any {
    return this.listTypeLoad;
  }

  async loadFile(){
    console.log(this.idSelectedType);
    //console.log("path en load",this.pathFile)
    try {
      if (this.idSelectedType == 1){
        console.log("carga de estudiantes")
        this.objectSend.tipo = "estudiante"
        this.objectSend.contenido = this.pathFile
        var response = await this.rest.PostRequest("carga", this.objectSend).toPromise();
        this.objectSend.tipo = "";
        this.objectSend.contenido = "";
        this.messageOk = response.message;
      }else if(this.idSelectedType == 2){
        console.log("carga de cursos pensum")
        this.objectSend.Cursos = this.pathFile
        var response = await this.rest.PostRequest("cursosPensum", this.objectSend).toPromise();
        this.objectSend.tipo = "";
        this.objectSend.contenido = "";
        this.messageOk = response.message;
      }else if(this.idSelectedType == 3){
        console.log("carga de cursos estudiatne");
        this.objectSend.tipo = "curso";
        this.objectSend.contenido = this.pathFile;
        var response = await this.rest.PostRequest("carga", this.objectSend).toPromise();
        this.objectSend.tipo = "";
        this.objectSend.contenido = "";
        this.messageOk = response.message;
      }else if(this.idSelectedType == 4){
        console.log("carga de apuntes");
        this.objectSend.tipo = "apuntes";
        this.objectSend.contenido = this.pathFile;
        var response = await this.rest.PostRequest("loadNotes", this.objectSend).toPromise();
        var response2 = await this.rest.GetRequest("reportHash").toPromise();
        this.objectSend.tipo = "";
        this.objectSend.contenido = "";
        this.messageOk = response.message;
      }
      //var response = await this.rest.PostRequest("")
    }catch (e: any) {
      this.messageError = e.error.message
    }
  }

  uploadFile(event:any){
    if(event.target.files && event.target.files[0]){
      var file = event.target.files[0]
      console.log("Mi file->",file);
      const reader = new FileReader();
      reader.onload = e => this.pathFile = reader.result;
      reader.readAsText(file, "utf-8")
    }
  }
  onSelected(id:number):void {
    this.selected = this.listTypeLoad.filter(item => item.id == id);
    //(change) = "onSelected($event.target.value)" en el select de html
  }

  closeAlert1(){
    this.messageOk = null;
  }

  closeAlert2(){
    this.messageError = null;
  }
}
