import { Component, OnInit } from '@angular/core';
import {RestService} from "../../services/rest.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-registerstudent',
  templateUrl: './registerstudent.component.html',
  styleUrls: ['./registerstudent.component.css']
})
export class RegisterstudentComponent implements OnInit {
  user = {
    carnet: "",
    DPI: "",
    nombre: "",
    carrera: "",
    correo: "",
    password: "",
    creditos: 0,
    edad: 0
  }
  messageOk = null
  messageError = null

  constructor(private rest:RestService, private route:Router) { }

  ngOnInit(): void {
  }

  async registerStudent(){
    try {
      var response = await this.rest.PostRequest("estudiante", this.user).toPromise();
      console.log(response);
      this.user.carnet = "";
      this.user.DPI = "";
      this.user.nombre = "";
      this.user.carrera = "";
      this.user.correo = "";
      this.user.password = "";
      this.user.creditos = 0;
      this.user.edad = 0;
      this.messageOk = response.message;
    }catch (e:any) {
      this.messageError = e.error.message;
    }
  }

  cancel() {
    this.route.navigate(["login"])
  }

  closeAlert1() {
    this.messageOk = null;
  }

  closeAlert2() {
    this.messageError = null;
  }

}
