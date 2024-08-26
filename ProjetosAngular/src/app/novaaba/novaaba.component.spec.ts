import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NovaabaComponent } from './novaaba.component';

describe('NovaabaComponent', () => {
  let component: NovaabaComponent;
  let fixture: ComponentFixture<NovaabaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [NovaabaComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NovaabaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
