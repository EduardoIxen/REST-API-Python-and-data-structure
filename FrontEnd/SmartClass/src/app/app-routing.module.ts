import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import {HomestudentComponent} from "./components/homestudent/homestudent.component";
import {HomeadminComponent} from "./components/homeadmin/homeadmin.component";
import {MenustudentComponent} from "./components/menustudent/menustudent.component";
import {LoginComponent} from "./components/login/login.component";
import {RegisterstudentComponent} from "./components/registerstudent/registerstudent.component";
import {LoadfileComponent} from "./components/loadfile/loadfile.component";
import {NotesStudentComponent} from "./components/notes-student/notes-student.component";
import {HashAdminComponent} from "./components/hash-admin/hash-admin.component";

//agregar todas las rutas del proyecto
const routes: Routes = [
  {path: "", component: LoginComponent},
  {path: "login", component: LoginComponent},
  {path: "registerStd", component: RegisterstudentComponent},
  {path: "homeStudent", component: HomestudentComponent},
  {path: "homeAdmin", component: HomeadminComponent},
  {path: "loadFile", component: LoadfileComponent},
  {path: "notesStudent", component: NotesStudentComponent},
  {path: "hashTable", component: HashAdminComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
