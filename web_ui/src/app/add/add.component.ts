// Import necessary modules
import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { FormControl, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { environment } from '../../environments/environment';

// Component decorator for x and y values
@Component({
  selector: 'app-add',
  templateUrl: './add.component.html',
  styleUrls: ['./add.component.sass'],
  standalone: true,
  imports: [ ReactiveFormsModule],

})

export class AddComponent {

  profileForm = new FormGroup({
    x : new FormControl(2, Validators.required),
    y : new FormControl(5, Validators.required)
  });



  constructor(private http: HttpClient) {}

  onSubmit() {
    // API from config
    this.http.post<any>('/api/add', { x:
    this.profileForm.value.x, y: this.profileForm.value.y   
    }).subscribe(data => {
      alert(JSON.stringify(data));
    });
  }
}





