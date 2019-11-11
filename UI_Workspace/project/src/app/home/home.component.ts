import { Component, OnInit } from '@angular/core';
import { AmazingTimePickerService } from 'amazing-time-picker';
import { BsDatepickerModule } from 'ngx-bootstrap/datepicker';
import { ChartdataService } from '../Service/chartdata.service';
import { formatDate } from 'ngx-bootstrap/chronos/format';
import { Router } from '@angular/router';
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
    time = {
        "startdate": "",
        "enddate": "",
        "starttime":"",
        "endtime": ""
    };
   
    x: any;
    y: any;
    constructor(private atp: AmazingTimePickerService, private router: Router) {
    
}
   
  ngOnInit() {
    }
    open() {
        const amazingTimePicker = this.atp.open();
        amazingTimePicker.afterClose().subscribe(time => { console.log(time); });
    }
    
    formatDate(date) {
    var d = new Date(date),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate(),
        year = d.getFullYear();
        var year1 = new String(year);
        year1 = year1.substring(2,5);
    if (month.length < 2)
        month = '0' + month;
    if (day.length < 2)
        day = '0' + day;

        return [month, day, year1].join('/');
}
    save() {
        this.time.startdate = this.formatDate(this.time.startdate);
        this.time.enddate = this.formatDate(this.time.enddate);
        this.x = this.time.startdate + " " + this.time.starttime;
        this.y = this.time.enddate + " " + this.time.endtime;
        localStorage.setItem('starttime', this.x);
        localStorage.setItem('endtime', this.y);
        this.router.navigate(['graphs']);
        
    }
}
