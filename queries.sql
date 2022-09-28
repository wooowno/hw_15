create table breeds
(
    id integer primary key autoincrement,
    breed varchar(100)
);

create table colors
(
    id integer primary key autoincrement,
    color varchar(100)
);

create table outcome_types
(
    id integer primary key autoincrement,
    outcome_type varchar(100)
);

create table outcome_subtypes
(
    id integer primary key autoincrement,
    outcome_subtype varchar(100)
);

create table cats
(
    id integer primary key autoincrement,
    cat_id integer,
    name varchar(100),
    date_of_birth date,
    outcome_type_id integer,
    outcome_subtype_id integer,
    outcome_month_year varchar(100),
    foreign key (outcome_type_id) references outcome_type(id),
    foreign key (outcome_subtype_id) references outcome_subtypes(id)
);

create table cat_breed
(
    cat_id integer,
    breed_id integer,
    foreign key (cat_id) references cats(id),
    foreign key (breed_id) references breeds(id)
);

create table cat_color
(
    cat_id integer,
    color_id integer,
    foreign key (cat_id) references cats(id),
    foreign key (color_id) references colors(id)
);
