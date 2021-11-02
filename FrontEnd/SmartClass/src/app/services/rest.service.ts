import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import {CookieService} from "ngx-cookie-service";

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json'
  }),
  body:{}
};

const address = 'http://localhost:3000/';
//manejo de la coneccion de las peticiones con el backend
@Injectable({
  providedIn: 'root'
})
export class RestService {
  private userLogged = null;

  constructor(private httpClient: HttpClient, private cookies: CookieService) { }

  PostRequest(serverAddress:string, info:object):Observable<any>{
    console.log(serverAddress);
    return this.httpClient.post<any>(address + serverAddress, info, httpOptions)
  }

  GetRequest(serverAddress: string): Observable<any> {
    console.log(serverAddress);
    return this.httpClient.get<any>(address + serverAddress, httpOptions);
  }

  PutRequest(serverAddress: string, info: object): Observable<any> {
    console.log(serverAddress);
    return this.httpClient.put<any>(address + serverAddress, info, httpOptions);
  }

  DeleteRequest(serverAddress: string): Observable<any> {
    console.log(serverAddress);
    return this.httpClient.delete<any>(address + serverAddress, httpOptions);
  }

  setToken(token: string){
    this.cookies.set("token", token);
  }
  getToken(){
    return this.cookies.get("token");
  }

  setUserLogged(user: any){
    this.userLogged = user;
  }

  getUserLogged(){
    return this.userLogged;
  }

  logout(){
    this.cookies.delete("token");
    this.userLogged = null;
  }
}
