import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {HttpClientModule} from "@angular/common/http";
import { RestService } from './services/rest.service';
import { FormsModule } from '@angular/forms';
import { HomestudentComponent } from './components/homestudent/homestudent.component';
import { MenustudentComponent } from './components/menustudent/menustudent.component';
import { MenuadminComponent } from './components/menuadmin/menuadmin.component';
import { HomeadminComponent } from './components/homeadmin/homeadmin.component';
import { LoginComponent } from './components/login/login.component';
import { RegisterstudentComponent } from './components/registerstudent/registerstudent.component';
import { MenuhomeComponent } from './components/menuhome/menuhome.component';
import { LoadfileComponent } from './components/loadfile/loadfile.component';
import {CookieService} from "ngx-cookie-service";
import { NotesStudentComponent } from './components/notes-student/notes-student.component';
import { HashAdminComponent } from './components/hash-admin/hash-admin.component';
import { PensumAdminComponent } from './components/pensum-admin/pensum-admin.component';
import { SearchcourseStudentComponent } from './components/searchcourse-student/searchcourse-student.component';

@NgModule({
  declarations: [
    //aca agregar todos los componentes que voy creando
    AppComponent,
    HomestudentComponent,
    MenustudentComponent,
    MenuadminComponent,
    HomeadminComponent,
    LoginComponent,
    RegisterstudentComponent,
    MenuhomeComponent,
    LoadfileComponent,
    NotesStudentComponent,
    HashAdminComponent,
    PensumAdminComponent,
    SearchcourseStudentComponent,
  ],
  imports: [
    FormsModule,
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [
    //agregar mis servicios
    RestService,
    CookieService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
