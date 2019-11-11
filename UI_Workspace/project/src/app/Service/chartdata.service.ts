import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class ChartdataService {
    
    constructor(private http: HttpClient) { }
    requestdata(x, y) {
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            "Access-Control-Allow-Methods":"GET, POST, DELETE, PUT"
        });
        let url1 = "http://localhost:5000/config-prediction/api/v1.0/service/all-data?start_time="+x+"&end_time="+y;
        return this.http.get(url1, { headers: headers });
    }
    popularConfiguration(x, y) {
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            "Access-Control-Allow-Methods": "GET, POST, DELETE, PUT"
        });
        console.log(x)
        let url1 = "http://localhost:5000/config-prediction/api/v1.0/service/config-data?start_time="+x+"&end_time="+y;
        return this.http.get(url1, { headers: headers });
    }
    efficiency(x, y) {
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            "Access-Control-Allow-Methods": "GET, POST, DELETE, PUT"
        });
        console.log(x)
        let url1 = "http://localhost:5000/config-prediction/api/v1.0/service/efficiency?start_time=" + x + "&end_time=" + y;
        return this.http.get(url1, { headers: headers });
    }
    retention(x, y) {
        let headers = new HttpHeaders({
            'Content-Type': 'application/json',
            "Access-Control-Allow-Methods": "GET, POST, DELETE, PUT"
        });
        console.log(x)
        let url1 = "http://localhost:5000/config-prediction/api/v1.0/service/retention?start_time=" + x + "&end_time=" + y;
        return this.http.get(url1, { headers: headers });
    }
}
