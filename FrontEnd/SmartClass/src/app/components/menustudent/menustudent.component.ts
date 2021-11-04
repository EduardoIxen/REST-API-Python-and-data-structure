import { Component, OnInit } from '@angular/core';
import {RestService} from "../../services/rest.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-menustudent',
  templateUrl: './menustudent.component.html',
  styleUrls: ['./menustudent.component.css']
})
export class MenustudentComponent implements OnInit {
  nameUser: string | null = "";
  constructor(private rest: RestService, private route: Router) { }

  ngOnInit(): void {
      this.nameUser = localStorage.getItem("name");
  }

  logout(){
    this.rest.logout();
    localStorage.clear();
    this.route.navigate(['/login']);
  }

}
