import { Component, OnInit } from '@angular/core';
import {RestService} from "../../services/rest.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-menuadmin',
  templateUrl: './menuadmin.component.html',
  styleUrls: ['./menuadmin.component.css']
})
export class MenuadminComponent implements OnInit {

  constructor(private rest: RestService, private route: Router) { }

  ngOnInit(): void {
  }

  logout(){
    this.rest.logout();
    localStorage.clear()
    this.route.navigate(['/login']);
  }

}
