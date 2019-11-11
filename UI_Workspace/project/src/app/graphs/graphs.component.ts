import { Component, OnInit } from '@angular/core';
import { ChartdataService } from '../Service/chartdata.service';
import { SidebarModule } from 'ng-sidebar';
import { ChartsModule } from 'ng2-charts';
import { ChartOptions, ChartType, ChartDataSets } from 'chart.js';
import { Label, SingleDataSet } from 'ng2-charts';

@Component({
  selector: 'app-graphs',
  templateUrl: './graphs.component.html',
  styleUrls: ['./graphs.component.css']
})
export class GraphsComponent implements OnInit {
    x: any;
    y: any;
    customerid = "";
    arr = [];
    uniqueNames = [];
    arr5 = [];
    pieChartLabels= [];
    pieChartData = [];
    barChartLabels: Label[] = [];
    public barChartType: ChartType = 'bar';
    public barChartData: ChartDataSets[] = [
        { data: [], label: 'Series A' },
    ];
    public barChartOptions: ChartOptions = {
        responsive: true,
        // We use these empty structures as placeholders for dynamic theming.
        scales: { xAxes: [{}], yAxes: [{}] },
        plugins: {
            datalabels: {
                anchor: 'end',
                align: 'end',
            }
        }
    };
    arr1=[]
    arr2 = [{ "count": "", "product_name": "" }];
    arr4=[]
    g1: boolean = false; g2: boolean = false; g3: boolean = false; g4: boolean = false; g5: boolean = false;
    sg1v: boolean = false; sg2v: boolean = false; sg3v: boolean = false; sg4v: boolean = false; sg5v: boolean = false;
    retain: boolean = false;

    constructor(private chartdata: ChartdataService ) {
        this.x = localStorage.getItem('starttime');
        this.y = localStorage.getItem('endtime');
        console.log(this.x);
    }
    public barChartOptions4: ChartOptions = {
        responsive: true,
        // We use these empty structures as placeholders for dynamic theming.
        scales: { xAxes: [{}], yAxes: [{}] },
        plugins: {
            datalabels: {
                anchor: 'end',
                align: 'end',
            }
        }
    };
    public barChartLabels4: Label[] = ['Product 1', 'Product 2', 'Product 3', 'Product 4', 'Product 5'];
    public barChartType4: ChartType = 'bar';
    public barChartLegend1 = true;
    public polarAreaChartLabels: Label[] = ['Success', 'Cancelled','Failure'];
    public polarAreaChartData: SingleDataSet = [];
    public polarAreaLegend = true;

    public polarAreaChartType: ChartType = 'polarArea';


    public barChartData4: ChartDataSets[] = [
        { data: [], label: 'Success' },
        { data: [], label: 'Failure' }
    ];

    switchon(event) {

        let target = event.target;
        let id = target.attributes.id;
        if (id.value == "g1") {
            this.g1 = true;
            this.g2 = false;
            this.g3 = false;
            this.g4 = false;
            this.g5 = false;
            this.arr = [];
            this.chartdata.requestdata(this.x, this.y).subscribe((data: any[]) => {
                
                
                for (let i = 0; i < data.length; i++) {
                    this.arr[i] = JSON.parse(data[i]);
                }
                console.log(this.arr[1].count);
                this.createLabels(this.arr)
                
            })
        }
        if (id.value == "g2") {
            this.g2 = true;
            this.g1 = false;
            this.g3 = false;
            this.g4 = false;
            this.g5 = false;

            
        }
        if (id.value == "g3") {
            this.g1 = false;
            this.g2 = false;
            this.g3 = true;
            this.g4 = false;
            this.g5 = false;
        }
        if (id.value == "g4") {
            this.g1 = false;
            this.g2 = false;
            this.g3 = false;
            
            this.g5 = false;
            this.chartdata.efficiency(this.x, this.y).subscribe((data: any[]) => {
                for (let i = 0; i < data.length; i++) {
                    this.arr4[i] = JSON.parse(data[i]);
                }
                let result1 = this.filterDataEff(this.arr4, 'Product 1', 'SUCCESS');
                let result2 = this.filterDataEff(this.arr4, 'Product 2', 'SUCCESS');
                let result3 = this.filterDataEff(this.arr4, 'Product 3', 'SUCCESS');
                let result4 = this.filterDataEff(this.arr4, 'Product 4', 'SUCCESS');
                let result5 = this.filterDataEff(this.arr4, 'Product 5', 'SUCCESS');
                console.log(result1)
                this.barChartData4[0].data[0] = result1[0].count;
                this.barChartData4[0].data[1] = result2[0].count;
                this.barChartData4[0].data[2] = result3[0].count;
                this.barChartData4[0].data[3] = result4[0].count;
                this.barChartData4[0].data[4] = result5[0].count;
                let result1c = this.filterDataEff(this.arr4, 'Product 1', 'CANCELLED');
                let result2c = this.filterDataEff(this.arr4, 'Product 2', 'CANCELLED');
                let result3c = this.filterDataEff(this.arr4, 'Product 3', 'CANCELLED');
                let result4c = this.filterDataEff(this.arr4, 'Product 4', 'CANCELLED');
                let result5c = this.filterDataEff(this.arr4, 'Product 5', 'CANCELLED');
                this.barChartData4[1].data[0] = result1c[0].count;
                this.barChartData4[1].data[1] = result2c[0].count;
                this.barChartData4[1].data[2] = result3c[0].count;
                this.barChartData4[1].data[3] = result4c[0].count;
                this.barChartData4[1].data[4] = result5c[0].count;
            })
            this.g4 = true;
        }
        if (id.value == "g5") {
            this.g1 = false;
            this.g2 = false;
            this.g3 = false;
            this.g4 = false;
            this.arr5 = [];
            this.chartdata.retention(this.x, this.y).subscribe((data: any[]) => {
                for (let i = 0; i < data.length; i++) {
                    this.arr5[i] = JSON.parse(data[i]);
                }
                for (let i = 0; i < this.arr5.length; i++) {

                    if (this.uniqueNames.indexOf(this.arr5[i].customer_id) === -1) {
                     
                        this.uniqueNames.push(this.arr5[i].customer_id);
                    }

                }
            });
            this.g5 = true;

        }
    }
    getgraph(event) {
        let target = event.target;
        let id = target.attributes.id;
        this.polarAreaChartData=[]
        let x = this.filterDataretain(this.arr5, this.customerid);
        let s = this.filterDateretainS(x, "SUCCESS");
        let c = this.filterDateretainS(x, "CANCELLED");
        let f = this.filterDateretainS(x, "FAILURE");
        if(s)
          this.polarAreaChartData.push(s[0].count);
        if (c.length==0) {
            this.polarAreaChartData.push(0);
        }
        else {
            
            this.polarAreaChartData.push(c[0].count);
        }
        if(f.count==0)
            this.polarAreaChartData.push(0);
        else
          this.polarAreaChartData.push(f[0].count);
        if (id.value == "submit")
            this.retain = true;
    }
    getresult(event) {
        let target = event.target;
        let id = target.attributes.id;
        this.chartdata.popularConfiguration(this.x, this.y).subscribe((data: any[]) => {
            console.log(data)
            for (let i = 0; i < data.length; i++) {
                this.arr1[i] = JSON.parse(data[i]);
            }
            this.barChartData = [
                { data: [], label: 'Configuration' },
            ];
            if (id.value == "sg1") {
                let result = this.filterData(this.arr1, "Product 1");
                for (let i = 0; i < result.length; i++) {
                    this.barChartLabels[i] = result[i].configuration;
                    this.barChartData[0].data[i] = result[i].count;
                    this.sg1v = true;
                    this.sg2v = false;
                    this.sg3v = false;
                    this.sg4v = false;
                    this.sg5v = false;
                    
                }
                
                
            }
            if (id.value == "sg2") {
                let result = this.filterData(this.arr1, "Product 2");
                for (let i = 0; i < result.length; i++) {
                    this.barChartLabels[i] = result[i].configuration;
                    this.barChartData[0].data[i] = result[i].count;
                    this.sg1v = false;
                    this.sg2v = true;
                    this.sg3v = false;
                    this.sg4v = false;
                    this.sg5v = false;

                }
                
            }
            if (id.value == "sg3") {
                let result = this.filterData(this.arr1, "Product 3");
                for (let i = 0; i < result.length; i++) {
                    this.barChartLabels[i] = result[i].configuration;
                    this.barChartData[0].data[i] = result[i].count;
                    this.sg1v = false;
                    this.sg2v = false;
                    this.sg3v = true;
                    this.sg4v = false;
                    this.sg5v = false;

                }
                
            }
            if (id.value == "sg4") {
                let result = this.filterData(this.arr1, "Product 4");
                for (let i = 0; i < result.length; i++) {
                    this.barChartLabels[i] = result[i].configuration;
                    this.barChartData[0].data[i] = result[i].count;
                    this.sg1v = false;
                    this.sg2v = false;
                    this.sg3v = false;
                    this.sg4v = true;
                    this.sg5v = false;

                }
                
            }
            if (id.value == "sg5") {
                let result = this.filterData(this.arr1, "Product 5");
                for (let i = 0; i < result.length; i++) {
                    this.barChartLabels[i] = result[i].configuration;
                    this.barChartData[0].data[i] = result[i].count;
                    this.sg1v = false;
                    this.sg2v = false;
                    this.sg3v = false;
                    this.sg4v = false;
                    this.sg5v = true;

                }
                
            }
        } )
    }
   filterData(data,locationName) {
    return data.filter(object => {
        return object['product_name'] == locationName;
    });
    }
    filterDataEff(data, productname,status) {
        let x;
        x=data.filter(object => {
           return object['product_name'] == productname;
           
         });
       return x.filter(object => {
            return object['result']== status
        })
    }
    filterDataretain(data,customerid) {
        return data.filter(object => {
            return object['customer_id'] == customerid;
        });
    }
    filterDateretainS(data, status) {
        return data.filter(object => {
            return object['result'] == status;
        });
    }
    
    createLabels(arr) {
        this.pieChartData = [];
        this.pieChartLabels = [];
        for (let i = 0; i < arr.length; i++) {
            //this.pieChartData[i] = +arr[i].count;
          
            this.pieChartData.push(arr[i].count);
            this.pieChartLabels.push(arr[i].product_name);
        }
    }
    public pieChartType: string = 'pie';
    public pieChartColors = [
        {
            backgroundColor: ['rgba(255,0,0,0.3)', ' rgba(255, 0, 0, 0.3)', 'rgba(0,0,255,0.3)', '#A52A2A', 'rgba(10,255,0,0.3)', 'rgba(10,255,0,0.3)', 'rgba(255,0,0,10)','	#008B8B'],
        },
    ];


    // events on slice click
    public chartClicked(e: any): void {
        console.log(e);
    }

    // event on pie chart slice hover
    public chartHovered(e: any): void {
        console.log(e);
    }
    
    pubarChartType = 'bar';
    barChartLegend = true;
    

   
  ngOnInit() {
  }

}
