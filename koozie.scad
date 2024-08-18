$fn=120;
difference() {
    cylinder(h=55, d1=72, d2=83);  // outer solid
    translate([0,0,6]) cylinder(h=50, d1=63, d2=72);  // inner cup
    translate([33.5,-4.25,38]) rotate([0,5.0,0]) cube([3, 8.5, 24.5]);
    }