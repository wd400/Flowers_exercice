import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpClientModule, HttpParams } from '@angular/common/http';

import { environment } from '../../environments/environment';
import { BrowserModule } from '@angular/platform-browser';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.sass'],
  providers:[
    HttpClientModule,
    CommonModule,
    BrowserModule
  ],
  standalone: true,
  imports: [HttpClientModule,
    CommonModule,
    BrowserModule
  ]



})
export class ListComponent {
  samples: any[] = [];
  page: number = 1; // default page
  maxPage: number =environment.maxPage;

  constructor(private http: HttpClient, private commonModule: CommonModule
    ) { }



    fetchSamples() {
      const params = new HttpParams().set('page', this.page.toString());
      this.http.get('/api/list', { params }).subscribe(response => {
  
        this.samples = response as any[];

  
      });
    }

    ngOnInit() {
      //execute only if on client side
      if (typeof window === 'undefined') {
        return;
      }
     this.fetchSamples();
    }
  


  changePage(page: number) {
    if (page < 1) {
      return;
    }
    this.page = page;
    this.fetchSamples();
  }

}