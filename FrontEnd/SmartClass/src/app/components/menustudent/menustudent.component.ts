import { Component, OnInit } from '@angular/core';
import {RestService} from "../../services/rest.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-menustudent',
  templateUrl: './menustudent.component.html',
  styleUrls: ['./menustudent.component.css']
})
export class MenustudentComponent implements OnInit {
  nameUser = "";
  constructor(private rest: RestService, private route: Router) { }

  ngOnInit(): void {
    if (this.rest.getUserLogged() != null){
      // @ts-ignore
      this.nameUser = this.rest.getUserLogged().name;
    }
  }

  logout(){
    this.rest.logout();
    this.route.navigate(['/login'])
  }

}
