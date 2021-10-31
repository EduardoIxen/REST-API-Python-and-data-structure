import { Component, OnInit } from '@angular/core';
import {RestService} from "../../services/rest.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  credentials = {
    user: "",
    password: ""
  };

  messageOk = null;
  messageError = null;

  constructor(private rest: RestService, private route: Router){}

  ngOnInit():void{
  }

  async login(){
    console.log(this.credentials.user)
    console.log(this.credentials.password)

    try {
      // peticion
      // podemos utilizar await o no
      var res = await this.rest.PostRequest("login", this.credentials).toPromise();
      console.log(res)
      this.credentials.user = "";
      this.credentials.password = "";
      this.messageOk = res.message;
      console.log("llego")
      if (res.type == "admin"){
        await this.route.navigate(['/homeAdmin'])
      }
      if(res.type == "student"){
        await this.route.navigate(['/','homeStudent']);
      }

    } catch (error:any) {
      this.messageError = error.error.message;
    }
  }

  closeAlert1(){
    this.messageOk = null;
  }

  closeAlert2(){
    this.messageError = null;
  }

}
