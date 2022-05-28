class Order{
    int id;
    String name;
    String courier;
    String time;
    int type;

    public Order(int id, String name, String courier, String time, int type) {
        super();
        this.id = id;
        this.name = name;
        this.courier = courier;
        this.time = time;
        this.type = type;
    }
    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public String getCourier() {
        return courier;
    }
    public void setCourier(String courier) {
        this.courier = courier;
    }
    public String getTime() {
        return time;
    }
    public void setTime(String time) {
        this.time = time;
    }
    public int getType() {
        return type;
    }
    public void setType(int type) {
        this.type = type;
    }
    @Override
    public String toString() {
        return "Order [id=" + id + ", name=" + name + ", courier=" + courier + ", time=" + time + ", type=" + type
                + "]";
    }
}
