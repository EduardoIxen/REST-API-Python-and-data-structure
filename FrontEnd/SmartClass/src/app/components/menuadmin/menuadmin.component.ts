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

  async generateReport(){
    try {
      var response = await this.rest.GetRequest("reportHash").toPromise();
    }catch (e) {
      console.log("Error al generar mensaje");
    }
  }

  async generateReportPensum(){
    try{
      var response = await this.rest.GetRequest("cursosPensum").toPromise();
    }catch (e) {
      console.log("Error al generar grafo de cursos del pensum");
    }

  }

}
