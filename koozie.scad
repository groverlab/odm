$fn=120;
difference() {
    cylinder(h=55, d1=72, d2=83);
    translate([0,0,6]) cylinder(h=50, d1=62, d2=73);
    translate([33,-4.25,33]) rotate([0,6.4,0]) cube([3, 8.5, 24.5]);
    }