import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ConfigrequestComponent } from './configrequest.component';

describe('ConfigrequestComponent', () => {
  let component: ConfigrequestComponent;
  let fixture: ComponentFixture<ConfigrequestComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ConfigrequestComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ConfigrequestComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
