import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { Router, RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule, provideHttpClient, withFetch } from '@angular/common/http';

//FormsModule,ReactiveFormsModule,BrowserModule

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [ HttpClientModule
    ,
   CommonModule,
    RouterModule,
 
    

    
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.sass',

})
export class AppComponent {
  title = 'INRIA Flowers Exercice';

  constructor(private router: Router) {  }

  get routes() {
    return this.router.config;
  }

}
