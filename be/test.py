data = [
    {
        "_id": "SGN-AHAPRO",
        "enable": True,
        "order": 1,
        "city_id": "SGN",
        "name": "Siêu Cấp",
        "rebroadcast_interval": 1200,
        "broadcast_distance": 2000,
        "name_vi_vn": "Siêu Cấp",
        "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/aha-service/AhaPro.png",
        "map_icon_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/core_services/xe1-02.png",
        "committed_time_formula": "if ( x <= 6 ) {60} else {((x -6) * 5 + 60)}",
        "commission_type": "PERCENTAGE",
        "commission_value": 0.212,
        "distance_fee": "(25000 if x <= 4 else 25000 + (x - 4) * 5500)",
        "stop_fee": 5500,
        "premium_service_fee": 7000,
        "partner": True,
        "require_pop": True,
        "pop_type": "photo",
        "require_poc": True,
        "poc_type": "photo",
        "require_pod": True,
        "pod_type": "photo",
        "name_en_us": "AHAPRO",
        "require_to": True,
        "auto_assign": False,
        "auto_assign_distance": 1000,
        "auto_assign_districts": [
            "VN.HC.QA",
            "VN.HC.QC",
            "VN.HC.QD",
            "VN.HC.QE",
            "VN.HC.QJ",
            "VN.HC.QK",
            "VN.HC.TB",
            "VN.HC.PN",
            "VN.HC.BH",
            "VN.HC.TP"
        ],
        "timeout": 1800,
        "cod": 10000000,
        "first_order_cod": 1,
        "advance_broadcast_distance": 2000,
        "max_stop_points": 5,
        "pool_timeout": 6300,
        "pool_timeout_commission_value": 0.3,
        "max_concurrent_orders": 1,
        "fee_description_en_us": "Thời gian: tối đa 1 giờ (áp dụng đơn hàng dưới 6km)\n\nSố điểm giao tối đa: 5\nPhí mỗi điểm giao thêm: 5,500đ\n\nPhí quãng đường:\n- 4km đầu: 25,000đ\n- Trên 4km: 5,500đ/km\n\nPhí giao hàng cao cấp: 7,000đ\n\nTrọng lượng tiêu chuẩn: 30kg\nKích thước tiêu chuẩn: 50x40x50 cm\n\nMức COD tối đa: 10,000,000đ\nPhí COD:\n- COD < 2,000,000đ: Miễn phí\n- COD >= 2,000,000đ: 0.88% * giá trị COD",
        "description_en_us": "Giao hàng nội thành trong 1 giờ",
        "description_vi_vn": "Giao hàng nội thành trong 1 giờ",
        "fee_description_vi_vn": "Thời gian: tối đa 1 giờ (áp dụng đơn hàng dưới 6km)\n\nSố điểm giao tối đa: 5\nPhí mỗi điểm giao thêm: 5,500đ\n\nPhí quãng đường:\n- 4km đầu: 25,000đ\n- Trên 4km: 5,500đ/km\n\nPhí giao hàng cao cấp: 7,000đ\n\nTrọng lượng tiêu chuẩn: 30kg\nKích thước tiêu chuẩn: 50x40x50 cm\n\nMức COD tối đa: 10,000,000đ\nPhí COD:\n- COD < 2,000,000đ: Miễn phí\n- COD >= 2,000,000đ: 0.88% * giá trị COD",
        "supplier_description": "Dịch vụ Siêu Cấp được thực hiện trong vòng 45 phút, được nhận tối đa 1 đơn hàng",
        "notify_package_return": True,
        "pending_period": 180,
        "cross_service": {
            "enable": True,
            "services": [
                "SGN-BIKE",
                "SGN-FOOD",
                "SGN-EXPRESS",
                "SGN-GOSHOP",
                "SGN-BIKE-INTRADISTRICT"
            ]
        },
        "event_callback": False,
        "uniform_verify_message_vi_vn": "Tài xế có mang đồng phục (áo, nón) hay không?",
        "uniform_verify_message_en_us": "Is your driver wearing proper uniform (including AhaMove's jacket, helmet)?",
        "uniform_verify": False,
        "rebroadcast_limit": 1,
        "last_valid_ro_hour": 18,
        "max_cod": 30000000,
        "max_cod_per_stop_point": 10000000,
        "max_item_value": 30000000,
        "cod_commission": {
            "value": 0.0088,
            "none_commission_limit": 2000000
        },
        "delay_time": 3,
        "cross_city": {
            "enable": True,
            "cities": [
                "SGN",
                "THD",
                "BHC"
            ]
        },
        "available_districts": [
            "VN.HC.TD",
            "VN.HC.CG",
            "VN.HC.GV",
            "VN.HC.QK",
            "VN.HC.QC",
            "VN.HC.TB",
            "VN.HC.QF",
            "VN.HC.QG",
            "VN.HC.TD",
            "VN.HC.BT",
            "VN.HC.TP",
            "VN.HC.QH",
            "VN.HC.QJ",
            "VN.HC.HM",
            "VN.HC.CC",
            "VN.HC.PN",
            "VN.HC.QE",
            "VN.HC.TD",
            "VN.HC.BH",
            "VN.HC.QA",
            "VN.HC.QD",
            "VN.HC.NB",
            "VN.HC.BC",
            "VN.HC.QL",
            "VN.BC",
            "VN.TA",
            "VN.BH",
            "VN.TDM",
            "VN.TU",
            "VN.DA",
            "VN.VT.VT",
            "VN.VT.BR"
        ],
        "delivery_type": "INSTANT",
        "map_icon_3d": {
            "url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/aha-vehicle/Icon_3D_BIKE.png",
            "sprite_size": 128,
            "sprite_count": 64
        },
        "note": "Giao diện mục Tổng phí đã được cập nhật.  Đối tác vui lòng chạm vào mục Tổng phí để xem chi tiết số tiền mặt (Nhận tiền mặt) cần thu từ phía khách hàng.",
        "payment_method": [
            {
                "description": "Cash",
                "description_vi_vn": "Tiền mặt",
                "payment": "cash",
                "order": 1
            },
            {
                "description": "Balance",
                "description_vi_vn": "Ví AhaMove",
                "payment": "balance",
                "order": 2
            },
            {
                "description": "MoMo e-Wallet",
                "description_vi_vn": "Ví điện tử MoMo",
                "payment": "momo",
                "order": 3
            },
            {
                "description": "ZaloPay e-Wallet",
                "description_vi_vn": "Ví điện tử\n\nÝ QC AhaMove, [4/22/2022 9:12 AM]\nZaloPay",
                "payment": "Zalopay",
                "order": 4
            }
        ],
        "enable_platform": [
            "momo_deeplink",
            "momo_permission",
            "zalo",
            "zalopay",
            "smartpay_deeplink",
            "viettel-pay_deeplink",
            "shopee-pay_deeplink"
        ],
        "same_district_delivery": False,
        "advance_max_concurrent_orders": 1,
        "applied_pandemic_hours_areas": [
            "VN.BH",
            "VN.PC.BT",
            "VN.PC.NK",
            "VN.PC.CR",
            "VN.PC.VT",
            "VN.PC.PD",
            "VN.PC.TN",
            "VN.PC.TL",
            "VN.PC.CD",
            "VN.PC.OM"
        ],
        "assigning_list_order": 3,
        "same_district_delivery_areas": [
            "VN.HCM.ZONE"
        ],
        "supplier_description_vi_vn": "Dịch vụ Siêu Cấp được thực hiện trong vòng 45 phút, được nhận tối đa 1 đơn hàng",
        "group_name_en_us": "Giao hàng chất lượng cao",
        "group_name_vi_vn": "Giao hàng chất lượng cao",
        "recommendation_config": {
            "supplier_timeout": 20,
            "recommend_timeout": 60,
            "recommend_radius": 1000,
            "sleep_interval": 60,
            "dispatch_mode": "RECOMMEND",
            "pool_mode": "NO_POOL",
            "pool_saving_threshold": 0.2,
            "poolable": False
        },
        "supplier_description_url": "https://ahamove.com/quy-trinh-giao-hang-dich-vu-co-ban",
        "distance_fee_v3": {
            "blocks": [
                {
                    "from": 0,
                    "to": 4,
                    "base": 25000,
                    "price_multiplier": 0
                },
                {
                    "from": 4,
                    "to": 100000,
                    "base": 25000,
                    "price_multiplier": 5500
                }
            ],
            "hour_rates": []
        },
        "vat_rate": 0.1,
        "priority_score": 4,
        "is_tip_allowed": True,
        "parent_id": "",
        "route_api_url": "https://apistg.ahamove.com/api/v3/internal/osrm/car/route/v1/driving/",
        "group_id": "AHAPRO",
        "animated_url": "https://i.imgur.com/xiDxEYN.png",
        "requests": [
            {
                "_id": "SGN-AHAPRO-INSURANCE",
                "name": "Khai giá hàng hoá",
                "name_vi_vn": "Khai giá hàng hoá",
                "name_en_us": "Value declaration",
                "enable": True,
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/Insurance/secure+24x24%402x.png",
                "order": 1,
                "price_blocks": [
                    {
                        "from": 0,
                        "to": 10000001,
                        "price": 5000,
                        "description_vi_vn": "Bồi thường mất mát hoặc hư hỏng theo giá trị hàng hoá của bạn",
                        "description_en_us": "Coverage for loss or damage according to the value of your items"
                    },
                    {
                        "from": 10000001,
                        "to": 20000001,
                        "price": 10000,
                        "description_vi_vn": "Bồi thường mất mát hoặc hư hỏng theo giá trị hàng hoá của bạn",
                        "description_en_us": "Coverage for loss or damage according to the value of your items"
                    },
                    {
                        "from": 20000001,
                        "to": 1000000000,
                        "price": 15000,
                        "description_vi_vn": "Bồi thường mất mát hoặc hư hỏng theo giá trị hàng hoá của bạn",
                        "description_en_us": "Coverage for loss or damage according to the value of your items"
                    }
                ],
                "no_supplier_payout": True,
                "type": "COD_INSURANCE",
                "applied_stp_num": 5,
                "service_id": "SGN-AHAPRO",
                "required_item_value": True,
                "description_url": "https://www.ahamove.com/aha-pro-cod-va-khai-gia/",
                "benefit_url": "https://www.ahamove.com/aha-pro-cod-va-khai-gia/",
                "non_cod_description": "Bồi thường mất mát hoặc hư hỏng theo danh mục hàng hoá của bạn",
                "none_cod_price_blocks": {
                    "electronics": 0,
                    "health & beauty": 0,
                    "housing & lifestyle": 0,
                    "food": 0,
                    "mother & baby": 0,
                    "fashion": 0,
                    "grocery": 0,
                    "restaurant": 0,
                    "sport": 0,
                    "drink": 0,
                    "other": 0,
                    "individual needs": 0,
                    "transportation": 0
                },
                "service_group_id": "AHAPRO",
                "group_id": "INSURANCE"
            },
            {
                "_id": "SGN-AHAPRO-BULKY",
                "name": "Giao hàng cồng kềnh",
                "enable": True,
                "support_remarks": True,
                "name_vi_vn": "Giao hàng cồng kềnh",
                "name_en_us": "Giao hàng cồng kềnh",
                "is_auto_assign_request": True,
                "icon_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/Special+Request/Special+Request+Icon/Bulky_packages.jpg",
                "order": 1,
                "tier_list": [
                    {
                        "code": "TIER_1",
                        "name_vi_vn": "Tiêu chuẩn",
                        "name_en_us": "Standard",
                        "selectable": False,
                        "price": 0,
                        "price_description_vi_vn": "Miễn phí",
                        "price_description_en_us": "Free",
                        "description_vi_vn": "50x40x50:30kg",
                        "description_en_us": "50x40x50:30kg",
                        "img_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/Special+Request/Bulky+Packages/Standard.png"
                    },
                    {
                        "code": "TIER_2",
                        "name_vi_vn": "Mức 1",
                        "name_en_us": "Package 1",
                        "price": 10000,
                        "selectable": True,
                        "description_vi_vn": "60x50x60:40kg",
                        "description_en_us": "60x50x60:40kg",
                        "img_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/Special+Request/Bulky+Packages/Tier+1.png"
                    },
                    {
                        "code": "TIER_3",
                        "name_vi_vn": "Mức 2",
                        "name_en_us": "Package 2",
                        "selectable": True,
                        "price": 20000,
                        "description_vi_vn": "70x60x70:60kg",
                        "description_en_us": "70x60x70:60kg",
                        "img_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/Special+Request/Bulky+Packages/Tier+2.png"
                    },
                    {
                        "code": "TIER_4",
                        "name_vi_vn": "Mức 3",
                        "name_en_us": "Package 3",
                        "selectable": True,
                        "price": 40000,
                        "description_vi_vn": "90x70x90:80kg",
                        "description_en_us": "90x70x90:80kg",
                        "img_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/Special+Request/Bulky+Packages/Tier+3.png"
                    },
                    {
                        "code": "TIER_MAX",
                        "name_vi_vn": "Quá tải trọng",
                        "name_en_us": "Over",
                        "selectable": False,
                        "price": -1,
                        "price_description_vi_vn": "Quá tải trọng",
                        "price_description_en_us": "Overload",
                        "description_vi_vn": "100x50x100cm (100kg)",
                        "description_en_us": "100x50x100cm (100kg)",
                        "warning_message": "Hàng hoá có kích thước lớn vượt quá quy định, không cho phép vận chuyển bằng xe máy",
                        "img_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/Special+Request/Bulky+Packages/Tier+max.png"
                    }
                ],
                "no_commission": False,
                "type": "TIER",
                "service_id": "SGN-AHAPRO",
                "img_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/Special+Request/Special+Request+Icon/Bulky_packages.jpg",
                "description_vi_vn": "Giao hàng cồng kềnh",
                "supplier_description_url": "https://ahamove.com/dichvukemtheo",
                "device_types": [
                    "web",
                    "android",
                    "ios"
                ],
                "supplier_description": "Hỗ trợ phí giao các món hàng có kích thước lớn",
                "service_group_id": "AHAPRO",
                "group_id": "BULKY"
            },
            {
                "_id": "SGN-AHAPRO-FRAGILE",
                "name": "Giao hàng dễ vỡ",
                "name_vi_vn": "Giao hàng dễ vỡ",
                "name_en_us": "Fragile items delivery",
                "icon_url": "https://ahamove.com/wp-content/uploads/2021/07/ic_fragile_256x256.png",
                "img_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/fragile-2x.png",
                "order": 1,
                "price": 10000,
                "description_vi_vn": "Dịch vụ này bảo vệ tối đa hàng hóa của bạn khi vận chuyển. Bạn muốn chúng tôi nâng niu mặt hàng nào dưới đây?",
                "description_en_us": "This service protects your items to the highest level during delivery. What items would you like us to take care of?",
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-AHAPRO",
                "enable": True,
                "supplier_description": "Hỗ trợ phí giao mặt hàng dễ vỡ, Đối tác vui lòng nhẹ tay và bảo quản cẩn thận mặt hàng.",
                "supplier_description_url": "https://ahamove.com/giao-hang-de-vo",
                "options": [
                    {
                        "code": "ITEM_1",
                        "name_vi_vn": "Bánh kem và các mặt hàng tương tự",
                        "name_en_us": "Cakes and similar items",
                        "selectable": True
                    },
                    {
                        "code": "ITEM_2",
                        "name_vi_vn": "Hoa và cây cảnh các loại",
                        "name_en_us": "Flowers and plants",
                        "selectable": True
                    },
                    {
                        "code": "ITEM_3",
                        "name_vi_vn": "Sản phẩm đựng trong chai/lọ/bình dễ vỡ",
                        "name_en_us": "Bottles and other breakable items",
                        "selectable": True
                    },
                    {
                        "code": "ITEM_4",
                        "name_vi_vn": "Sản phẩm làm bằng thủy tinh/gốm sứ/đất nung",
                        "name_en_us": "Glass, porcelain, pottery and other ceramics",
                        "selectable": True
                    },
                    {
                        "code": "ITEM_5",
                        "name_vi_vn": "Hàng hóa, thiết bị điện tử",
                        "name_en_us": "Electronic devices",
                        "selectable": True
                    },
                    {
                        "code": "ITEM_6",
                        "name_vi_vn": "Khác (vui lòng nêu rõ)",
                        "name_en_us": "Other (please specify)",
                        "selectable": True,
                        "need_user_input": True
                    }
                ],
                "max_distance": 10000,
                "service_group_id": "AHAPRO",
                "group_id": "FRAGILE"
            },
            {
                "_id": "SGN-AHAPRO-SMS",
                "name": " Gửi SMS cho người nhận",
                "enable": True,
                "support_remarks": True,
                "name_vi_vn": " Gửi SMS cho người nhận",
                "name_en_us": "Send SMS to recipient",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_d2d.png",
                "order": 1,
                "price": 1000,
                "no_supplier_payout": True,
                "type": "BOOLEAN",
                "service_id": "SGN-AHAPRO",
                "send_sms": True,
                "img_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_d2d.png",
                "sms_template": "Shipper AhaMove se giao don hang tu {actual_sender_name} toi quy khach trong vong {min_eta} - {max_eta} phut nua. Theo doi don hang tai: {shared_link}",
                "sms_template_v3": "Shipper AhaMove se giao don hang tu %s toi quy khach trong vong %s - %s phut nua. Theo doi don hang tai: %s",
                "description_vi_vn": "Giao hàng chuyên nghiệp hơn với dịch vụ nhắn tin SMS, giúp người nhận của bạn dễ dàng theo dõi đơn hàng mọi lúc mọi nơi",
                "description_en_us": "Deliver seamless customer experiences through SMS: let your recipients track their orders anytime and anywhere",
                "sms_demo": "<p>Shipper AhaMove se giao don hang tu <span style=\"color: #FF8200;\"><strong>Pizza 4P's</strong></span>&nbsp;toi quy khach trong vong <span style=\"color: #FF8200;\"><strong>18 - 25&nbsp;</strong></span>phut nua. Theo doi don hang tai:&nbsp;<span style=\"color: #FF8200;\"><strong>https://track.ahamove.com/203TG2NW</strong></span></p>",
                "device_types": [
                    "web",
                    "android",
                    "ios"
                ],
                "service_group_id": "AHAPRO",
                "group_id": "SMS"
            },
            {
                "_id": "SGN-AHAPRO-ROUND-TRIP",
                "name": "Quay lại điểm lấy hàng",
                "enable": True,
                "name_vi_vn": "Quay lại điểm lấy hàng",
                "name_en_us": "Return to pick up location",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_round_trip.png",
                "img_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_round_trip.png",
                "order": 1,
                "description_vi_vn": "Tài xế sẽ quay lại điểm lấy hàng với số phí bằng 80% phí khoảng cách. Lưu ý: Phí khoảng cách là số phí dựa theo số km vận chuyển, ko bao gồm phí điểm dừng và các loại phí khác.",
                "description_en_us": "Driver will return to pick up location for 80% of distance fee. Note: Distance fee is calculated solely by the travel distance, it does not include stop fee and others fee",
                "type": "COMMISSION_DISTANCE_PERCENTAGE",
                "price": 0.8,
                "description": "",
                "service_id": "SGN-AHAPRO",
                "supplier_description_vi_vn": "Đối tác tiến hành quay trở lại điểm lấy hàng sau khi giao thành công ",
                "supplier_description": "Đối tác tiến hành quay trở lại điểm lấy hàng sau khi giao thành công ",
                "supplier_description_url": "https://ahamove.com/dichvukemtheo",
                "service_group_id": "AHAPRO",
                "group_id": "TRIP"
            },
            {
                "_id": "SGN-AHAPRO-D2D",
                "name": "Giao hàng tận tay",
                "enable": True,
                "name_vi_vn": "Giao hàng tận tay",
                "name_en_us": "Giao hàng tận tay",
                "icon_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/core_services/req_d2d.png",
                "order": 3,
                "price": 10000,
                "no_commission": True,
                "type": "BOOLEAN",
                "service_id": "SGN-AHAPRO",
                "device_types": [
                    "web",
                    "ios",
                    "android"
                ],
                "delivery_option": True,
                "img_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/core_services/req_d2d.png",
                "description_vi_vn": "Khách hàng có thể chọn được từng điểm giao để yêu cầu tài xế giao hàng tới tận tay người nhận.",
                "description_en_us": "Khách hàng có thể chọn được từng điểm giao để yêu cầu tài xế giao hàng tới tận tay người nhận.",
                "description_url": "https://ahamove.com/gioi-thieu-tinh-nang-giao-hang-tan-tay/",
                "supplier_description_vi_vn": "Hỗ trợ phí giao tận tay đến khách hàng (VD: giao lên lầu,...)",
                "supplier_description": "Hỗ trợ phí giao tận tay đến khách hàng (VD: giao lên lầu,...)",
                "supplier_description_url": "https://ahamove.com/dichvukemtheo",
                "service_group_id": "AHAPRO",
                "group_id": "D2D"
            },
            {
                "_id": "SGN-AHAPRO-TIP",
                "name": "Hỗ trợ tài xế",
                "enable": True,
                "name_vi_vn": "Hỗ trợ tài xế",
                "name_en_us": "Tipping",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/sr_tipping.png",
                "img_url": "http://file.hstatic.net/1000010797/file/tipping_final.jpg",
                "order": 4,
                "no_commission": True,
                "description_vi_vn": "Hãy chọn dịch vụ này nếu bạn muốn hỗ trợ tài xế trong giờ cao điểm, khi thời tiết khó khăn, hoặc đơn giản là muốn thưởng thêm cho tài xế. Ngoài ra, tính năng này sẽ giúp cho đơn hàng của bạn được ưu tiên hơn trong thời gian cao điểm.",
                "description_en_us": "This will show your support or compliment to the driver, especially in rush hours, hand to hand delivery, bad weather. Also, this feature will prioritize your request in peak time.",
                "type": "PER_UNIT",
                "price": 5000,
                "description": "",
                "service_id": "SGN-AHAPRO",
                "max_input": 6,
                "no_promotion": True,
                "service_group_id": "AHAPRO",
                "group_id": "TIP"
            }
        ],
        "currency": "VND"
    },
    {
        "_id": "SGN-BIKE",
        "enable": True,
        "order": 1,
        "city_id": "SGN",
        "name": "Siêu Tốc",
        "rebroadcast_interval": 1200,
        "rebroadcast_limit": 2,
        "broadcast_distance": 500000,
        "complete_interval": 2,
        "name_vi_vn": "Siêu Tốc",
        "icon_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/aha-service/SieuToc.jpg",
        "map_icon_url": "https://ahamove.com/wp-content/uploads/2020/01/icon-tet.png",
        "distance_fee": "(25000 if x <= 4 else 25000 + (x - 4) * 5500)",
        "commission_type": "PERCENTAGE",
        "commission_value": 0.212,
        "max_distance": 100000,
        "stop_fee": 5500,
        "name_en_us": "Siêu Tốc",
        "require_to": True,
        "name_vi_VN": "Siêu Tốc",
        "auto_assign": False,
        "auto_assign_distance": 5000,
        "require_request": False,
        "advance_broadcast_distance": 500000,
        "timeout": 600,
        "cod": 10000000,
        "first_order_cod": 1,
        "max_stop_points": 5,
        "max_concurrent_orders": 1,
        "pending_period": 100,
        "fee_description_en_us": "Thời gian: tối đa 1 giờ (áp dụng với đơn hàng dưới 6km)\n\nSố điểm giao hàng tối đa: 5\n\nPhí mỗi điểm giao thêm: 5,000đ\nKhu vực giao: Giao liên quận\n\nPhí quãng đường:\n- 4 km đầu: 23,000đ\n- Trên 4 km: 5,000đ/km\n\nMức COD tối đa: 10,000,000đ\nPhí COD:\n- COD < 2,000,000đ: miễn phí\n- COD >= 2,000,000đ: 0,8% x Giá trị COD",
        "description_en_us": "Deliver within an hour",
        "description_vi_vn": "Giao hàng trong 1h",
        "fee_description_vi_vn": "Thời gian: tối đa 1 giờ (áp dụng với đơn hàng dưới 6km)\n\nSố điểm giao hàng tối đa: 5\n\nPhí mỗi điểm giao thêm: 5,000đ\nKhu vực giao: Giao liên quận\n\nPhí quãng đường:\n- 4 km đầu: 23,000đ\n- Trên 4 km: 5,000đ/km\n\nMức COD tối đa: 10,000,000đ\nPhí COD:\n- COD < 2,000,000đ: miễn phí\n- COD >= 2,000,000đ: 0,8% x Giá trị COD",
        "tooltips": {
            "ASSIGNING": {
                "message": [
                    "Đơn hàng của bạn đang được AhaMove xử lí. Sẽ có tài xế chấp nhận trong 5-10' tiếp theo!"
                ],
                "message_vi_vn": [
                    "Đơn hàng của bạn đang được AhaMove xử lí. Sẽ có tài xế chấp nhận trong 5-10' tiếp theo!"
                ]
            },
            "ACCEPTED": {
                "message": [
                    "Driver will arrive to your location within 15 minutes",
                    "Delivery time can take up to 2 hours"
                ],
                "message_vi_vn": [
                    "Tài xế sẽ đến chỗ bạn trong vòng 15 phút",
                    "Thời gian giao hàng có thể lên đến 2 tiếng"
                ]
            }
        },
        "parent_id": "SGN-GROUP-BIKE_EXPRESS",
        "supplier_description": "Giao hoả tốc trong 1h",
        "notify_package_return": True,
        "cross_service": {
            "enable": True,
            "services": [],
            "non-category": [
                "Corporation - Cake",
                "Corporation - Dry food"
            ]
        },
        "uniform_verify": True,
        "recommend_order": False,
        "event_callback": True,
        "uniform_verify_message_vi_vn": "Tài xế có mang đồng phục (áo, nón) hay không?",
        "uniform_verify_message_en_us": "Is your driver wearing proper uniform (including AhaMove's jacket, helmet)?",
        "recommendation_config": {
            "supplier_timeout": 20,
            "recommend_timeout": 20,
            "poolable": False,
            "recommend_radius": 700,
            "sleep_interval": 60,
            "dispatch_mode": "RECOMMEND",
            "pool_mode": "NO_POOL",
            "pool_saving_threshold": 0.2
        },
        "set_idle_status_when_creating_order": False,
        "need_confirm_before_pickup": False,
        "service_description_vi_vn": {
            "fee_desc": {
                "0-4km": 23000,
                "Mỗi km tiếp theo": 5000
            },
            "sla": {
                "COD tối đa": 500000,
                "Trọng lượng tối đa": "5kg",
                "Kích thước tối đa": "25(D) x 32(R) x 12(C) cm"
            },
            "more_details": [
                "Giá đã bao gồm VAT",
                "Nếu giao đồ ăn, xin vui lòng cân nhắc thời gian giao hàng"
            ]
        },
        "note": "1. Vui lòng gọi điện cho người nhận trước khi đến lấy hàng.\n2. Đơn hàng không cần ứng tiền COD, vẫn thu tiền COD từ người nhận và nộp lại qua MoMo/Tk Ahamove.\n3. Tài xế huỷ đơn thì phải gọi lên tổng đài. Tuyệt đối không lấy hàng đi nếu chưa gọi được cho người nhận.\n4. Olala.\n5. Olele.",
        "max_cod_per_stop_point": 1300000,
        "cod_commission": {
            "value": 0.0088,
            "none_commission_limit": 2000000
        },
        "max_cod": 10000001,
        "idle_timeout": 2,
        "committed_time_formula": "if ( x <= 6 ) {60} else {((x -6) * 5 + 60)}",
        "delivery_type": "INSTANT",
        "cross_city": {
            "enable": False,
            "cities": [
                "SGN"
            ]
        },
        "map_icon_3d": {
            "url": "https://files.ahamove.com/sgn-bike-v4.png",
            "sprite_size": 2000,
            "sprite_count": 64
        },
        "require_pof": True,
        "enable_upload_pof": True,
        "route_api_url": "https://apistg.ahamove.com/api/v3/internal/osrm/bike/route/v1/driving/",
        "enable_platform": [
            "momo_deeplink",
            "momo_permission",
            "zalo",
            "zalopay",
            "smartpay_deeplink",
            "viettel-pay_deeplink",
            "shopee-pay_deeplink",
            "onwheel",
            "vpbank_deeplink"
        ],
        "supplier_description_url": "https://ahamove.com/quy-trinh-giao-don-sieu-toc-sieu-re/",
        "limit_call": True,
        "distance_fee_v3": {
            "blocks": [
                {
                    "from": 0,
                    "to": 4,
                    "base": 25000,
                    "price_multiplier": 0
                },
                {
                    "from": 4,
                    "to": 100000,
                    "base": 25000,
                    "price_multiplier": 5500
                }
            ],
            "hour_rates": []
        },
        "group_name_en_us": "Fast delivery",
        "group_name_vi_vn": "Giao nhanh",
        "same_district_delivery": False,
        "available_districts": [
            "VN.HC.BC",
            "VN.HC.CC",
            "VN.HC.CG",
            "VN.HC.HM",
            "VN.HC.NB",
            "VN.HC.BH",
            "VN.HC.BT",
            "VN.HC.GV",
            "VN.HC.PN",
            "VN.HC.QJ",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.QA",
            "VN.HC.QB",
            "VN.HC.QC",
            "VN.HC.QD",
            "VN.HC.QE",
            "VN.HC.QF",
            "VN.HC.QG",
            "VN.HC.QH",
            "VN.HC.QI",
            "VN.HC.TB",
            "VN.HC.TP",
            "VN.HC.TD"
        ],
        "applied_pandemic_hours_areas": [
            "VN.HC.BC",
            "VN.HC.BH",
            "VN.HC.BT",
            "VN.HC.CG",
            "VN.HC.CC",
            "VN.HC.GV",
            "VN.HC.HM",
            "VN.HC.NB",
            "VN.HC.PN",
            "VN.HC.QA",
            "VN.HC.QJ",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.QB",
            "VN.HC.QC",
            "VN.HC.QD",
            "VN.HC.QE",
            "VN.HC.QF",
            "VN.HC.QG",
            "VN.HC.QH",
            "VN.HC.QI",
            "VN.HC.TD",
            "VN.HC.TB",
            "VN.HC.TP",
            "VN.HI.UH",
            "VN.HI.BD",
            "VN.HI.BTL",
            "VN.HI.CM",
            "VN.HI.CG",
            "VN.HI.GL",
            "VN.HI.HB",
            "VN.HI.HC",
            "VN.HI.HK",
            "VN.HI.HM",
            "VN.HI.HG",
            "VN.HI.LB",
            "VN.VC.ML",
            "VN.HI.MD",
            "VN.HI.NTL",
            "VN.HI.PX",
            "VN.HI.PT",
            "VN.HI.QO",
            "VN.HI.SS",
            "VN.HI.ST",
            "VN.HI.TO",
            "VN.HI.TT",
            "VN.HI.TX",
            "VN.HI.TN",
            "VN.HI.TC",
            "VN.HI.TH",
            "VN.HI.DP",
            "VN.HI.DA",
            "VN.HI.DD",
            "VN.HI.BV",
            "VN.BH",
            "VN.TDM",
            "VN.TA",
            "VN.DA",
            "VN.PC.BT",
            "VN.PC.NK",
            "VN.PC.CR",
            "VN.PC.VT",
            "VN.PC.PD",
            "VN.PC.TN",
            "VN.PC.TL",
            "VN.PC.CD",
            "VN.PC.OM"
        ],
        "assigning_list_order": 3,
        "same_district_delivery_areas": [
            "VN.HCM.ZONE",
            "VN.BH",
            "VN.VT.VT"
        ],
        "require_pod": True,
        "vat_rate": 0.1,
        "is_saas": False,
        "partner": False,
        "accept_message": "",
        "enable_cancellation_punishment": True,
        "priority_score": 2,
        "is_tip_allowed": True,
        "last_valid_rebroadcast_hour": 9,
        "next_valid_rebroadcast_hour": 10,
        "assigning_before_bk": [
            {
                "from": 0,
                "to": 18,
                "value": 3600
            },
            {
                "from": 16,
                "to": 20,
                "value": 600
            },
            {
                "from": 20,
                "to": 24,
                "value": 1800
            }
        ],
        "group_id": "BIKE",
        "animated_url": "https://i.imgur.com/xiDxEYN.png",
        "requests": [
            {
                "_id": "SGN-BIKE-POD",
                "name": "Thu hộ qua ví điện tử",
                "name_vi_vn": "Thu hộ qua ví điện tử",
                "name_en_us": "Collect payment via e-wallet",
                "price": 0,
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/icon-POD-extraservice.png",
                "img_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/IMG-POD-extraservice.png",
                "description_vi_vn": "Tài xế không cần ứng trước tiền thu hộ. Người nhận chỉ cần quét mã QR để thanh toán qua ví điện tử hoặc ứng dụng Mobile Banking khi tài xế đến giao hàng. Tiền thu hộ sẽ tự động chuyển vào tài khoản COD của bạn sau khi đơn hàng hoàn tất.",
                "description_en_us": "Your driver doesn't have to pay in advance. Upon delivery, the recipient scans a QR code to pay via an e-wallet or Mobile Banking app. Payment will be transferred to your COD account once the order is complete.",
                "type": "BOOLEAN",
                "description": "Người nhận thanh toán qua ví điện tử",
                "service_id": "SGN-BIKE",
                "enable": True,
                "no_commission": True,
                "subtype": "epayment_on_delivery",
                "applied_stp_num": 2,
                "max_pod": 1000000,
                "transfer_cod": True,
                "capital_coefficient": 1,
                "available_districts": [
                    "VN.HC.QA",
                    "VN.HC.QB",
                    "VN.HC.QC",
                    "VN.HC.QD",
                    "VN.HC.QE",
                    "VN.HC.QF",
                    "VN.HC.QG",
                    "VN.HC.QH",
                    "VN.HC.QI",
                    "VN.HC.QJ",
                    "VN.HC.QK",
                    "VN.HC.QL",
                    "VN.HC.BT",
                    "VN.HC.BH",
                    "VN.HC.GV",
                    "VN.HC.PN",
                    "VN.HC.TB",
                    "VN.HC.TP",
                    "VN.HC.TD",
                    "VN.HC.BC",
                    "VN.HC.CG",
                    "VN.HC.CC",
                    "VN.HC.HM",
                    "VN.HC.NB"
                ],
                "service_group_id": "BIKE",
                "group_id": "POD"
            },
            {
                "_id": "SGN-BIKE-ROUND-TRIP",
                "name": "Quay lại điểm lấy hàng",
                "name_vi_vn": "Quay lại điểm lấy hàng",
                "name_en_us": "Quay lại điểm lấy hàng",
                "enable": True,
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_round_trip.png",
                "img_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_round_trip.png",
                "order": 1,
                "description_vi_vn": "- Tài xế sẽ quay lại điểm lấy hàng với số phí bằng 80% phí khoảng cách.\n\n- Lưu ý: Phí khoảng cách là số phí dựa theo số km vận chuyển, ko bao gồm phí điểm dừng và các loại phí khác.",
                "description_en_us": "Driver will return to pick up location for 80% of distance fee. Note: Distance fee is calculated solely by the travel distance, it does not include stop fee and others fee",
                "type": "COMMISSION_DISTANCE_PERCENTAGE",
                "price": 0.8,
                "description": "",
                "supplier_description": "Tài xế sẽ quay lại điểm lấy hàng với số phí bằng 80% phí khoảng cách. Lưu ý: Phí khoảng cách là số phí dựa theo số km vận chuyển, ko bao gồm phí điểm dừng và các loại phí khác.",
                "service_id": "SGN-BIKE",
                "no_commission": False,
                "no_promotion": True,
                "service_group_id": "BIKE",
                "group_id": "TRIP"
            },
            {
                "_id": "SGN-BIKE-SMS",
                "name": " Gửi SMS cho người nhận",
                "enable": True,
                "support_remarks": True,
                "name_vi_vn": " Gửi SMS cho người nhận",
                "name_en_us": "Send SMS to recipient",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_d2d.png",
                "order": 1,
                "price": 1000,
                "no_supplier_payout": True,
                "type": "BOOLEAN",
                "service_id": "SGN-BIKE",
                "send_sms": True,
                "img_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_d2d.png",
                "sms_template": "Shipper AhaMove se giao don hang tu {actual_sender_name} toi quy khach trong vong {min_eta} - {max_eta} phut nua. Theo doi don hang tai: {shared_link}",
                "sms_template_v3": "Shipper AhaMove se giao don hang tu %s toi quy khach trong vong %s - %s phut nua. Theo doi don hang tai: %s",
                "description_vi_vn": "Giao hàng chuyên nghiệp hơn với dịch vụ nhắn tin SMS, giúp người nhận của bạn dễ dàng theo dõi đơn hàng mọi lúc mọi nơi",
                "description_en_us": "Deliver seamless customer experiences through SMS: let your recipients track their orders anytime and anywhere",
                "sms_demo": "<p>Shipper AhaMove se giao don hang tu <span style=\"color: #FF8200;\"><strong>Pizza 4P's</strong></span>&nbsp;toi quy khach trong vong <span style=\"color: #FF8200;\"><strong>18 - 25&nbsp;</strong></span>phut nua. Theo doi don hang tai:&nbsp;<span style=\"color: #FF8200;\"><strong>https://track.ahamove.com/203TG2NW</strong></span></p>",
                "service_group_id": "BIKE",
                "group_id": "SMS"
            },
            {
                "_id": "SGN-BIKE-BULKY",
                "name": "Giao hàng cồng kềnh",
                "enable": True,
                "is_auto_assign_request": True,
                "support_remarks": True,
                "name_vi_vn": "Giao hàng cồng kềnh",
                "name_en_us": "Giao hàng cồng kềnh",
                "icon_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/Special+Request/Special+Request+Icon/Bulky_packages.jpg",
                "order": 1,
                "tier_list": [
                    {
                        "code": "TIER_1",
                        "name_vi_vn": "Tiêu chuẩn",
                        "name_en_us": "Standard",
                        "selectable": False,
                        "price": 0,
                        "price_description_vi_vn": "Miễn phí",
                        "price_description_en_us": "Free",
                        "description_vi_vn": "50x40x50:30kg",
                        "description_en_us": "50x40x50:30kg",
                        "img_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/Special+Request/Bulky+Packages/Standard.png"
                    },
                    {
                        "code": "TIER_2",
                        "name_vi_vn": "Mức 1",
                        "name_en_us": "Package 1",
                        "price": 10000,
                        "selectable": True,
                        "description_vi_vn": "60x50x60:40kg",
                        "description_en_us": "60x50x60:40kg",
                        "img_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/Special+Request/Bulky+Packages/Tier+1.png"
                    },
                    {
                        "code": "TIER_3",
                        "name_vi_vn": "Mức 2",
                        "name_en_us": "Package 2",
                        "selectable": True,
                        "price": 20000,
                        "description_vi_vn": "70x60x70:60kg",
                        "description_en_us": "70x60x70:60kg",
                        "img_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/Special+Request/Bulky+Packages/Tier+2.png"
                    },
                    {
                        "code": "TIER_4",
                        "name_vi_vn": "Mức 3",
                        "name_en_us": "Package 3",
                        "selectable": True,
                        "price": 40000,
                        "description_vi_vn": "90x70x90:80kg",
                        "description_en_us": "90x70x90:80kg",
                        "img_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/Special+Request/Bulky+Packages/Tier+3.png"
                    },
                    {
                        "code": "TIER_MAX",
                        "name_vi_vn": "Quá tải trọng",
                        "name_en_us": "Over",
                        "selectable": False,
                        "price": -1,
                        "price_description_vi_vn": "Quá tải trọng",
                        "price_description_en_us": "Overload",
                        "description_vi_vn": "100x50x100cm (100kg)",
                        "description_en_us": "100x50x100cm (100kg)",
                        "warning_message": "Hàng hoá có kích thước lớn vượt quá quy định, không cho phép vận chuyển bằng xe máy",
                        "img_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/Special+Request/Bulky+Packages/Tier+max.png"
                    }
                ],
                "no_commission": False,
                "type": "TIER",
                "service_id": "SGN-BIKE",
                "img_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/Special+Request/Special+Request+Icon/Bulky_packages.jpg",
                "description_vi_vn": "Giao hàng cồng kềnh",
                "supplier_description_url": "https://ahamove.com/dichvukemtheo",
                "device_types": [
                    "web",
                    "android",
                    "ios"
                ],
                "supplier_description": "Hỗ trợ phí giao các món hàng có kích thước lớn",
                "group_service_id": "BIKE",
                "group_id": "BULKY",
                "service_group_id": "BIKE"
            },
            {
                "_id": "SGN-BIKE-FRAGILE",
                "name": "Giao hàng dễ vỡ",
                "enable": True,
                "is_auto_assign_request": True,
                "support_remarks": True,
                "name_vi_vn": "Giao hàng dễ vỡ",
                "name_en_us": "Fragile items delivery",
                "icon_url": "https://ahamove.com/wp-content/uploads/2021/07/ic_fragile_256x256.png",
                "order": 1,
                "price": 10000,
                "service_id": "SGN-BIKE",
                "type": "BOOLEAN",
                "img_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/fragile-2x.png",
                "description_vi_vn": "Dịch vụ này bảo vệ tối đa hàng hóa của bạn khi vận chuyển. Bạn muốn chúng tôi nâng niu mặt hàng nào dưới đây?",
                "description_en_us": "This service protects your items to the highest level during delivery. What items would you like us to take care of?",
                "title_description_vi_vn": "Hàng dễ vỡ đã có chúng tôi lo",
                "title_description_en_us": "Your items are in good hands",
                "supplier_description": "Hỗ trợ phí giao mặt hàng dễ vỡ, Đối tác vui lòng nhẹ tay và bảo quản cẩn thận mặt hàng",
                "supplier_description_url": "https://ahamove.com/",
                "options": [
                    {
                        "code": "ITEM_1",
                        "name_vi_vn": "Bánh kem và các mặt hàng tương tự",
                        "name_en_us": "Cakes and similar items",
                        "selectable": True
                    },
                    {
                        "code": "ITEM_2",
                        "name_vi_vn": "Hoa và cây cảnh các loại",
                        "name_en_us": "Flowers and plants",
                        "selectable": True
                    },
                    {
                        "code": "ITEM_3",
                        "name_vi_vn": "Sản phẩm đựng trong chai/lọ/bình dễ vỡ",
                        "name_en_us": "Bottles and other breakable items",
                        "selectable": True
                    },
                    {
                        "code": "ITEM_4",
                        "name_vi_vn": "Sản phẩm làm bằng thủy tinh/gốm sứ/đất nung",
                        "name_en_us": "Glass, porcelain, pottery and other ceramics",
                        "selectable": True
                    },
                    {
                        "code": "ITEM_5",
                        "name_vi_vn": "Hàng hóa, thiết bị điện tử",
                        "name_en_us": "Electronic devices",
                        "selectable": True
                    },
                    {
                        "code": "ITEM_6",
                        "name_vi_vn": "Khác (vui lòng nêu rõ)",
                        "name_en_us": "Other (please specify)",
                        "selectable": True,
                        "need_user_input": True
                    }
                ],
                "max_distance": 10000,
                "service_group_id": "BIKE",
                "group_id": "FRAGILE"
            },
            {
                "_id": "SGN-BIKE-INSURANCE",
                "name": "Khai giá hàng hoá",
                "name_vi_vn": "Khai giá hàng hoá",
                "name_en_us": "Value declaration",
                "enable": True,
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/Insurance/secure+24x24%402x.png",
                "order": 1.0,
                "price_blocks": [
                    {
                        "from": 0,
                        "to": 5000001,
                        "price": 1000,
                        "description_vi_vn": "Bồi thường mất mát hoặc hư hỏng theo giá trị hàng hoá của bạn",
                        "description_en_us": "Coverage for loss or damage according to the value of your items"
                    },
                    {
                        "from": 5000001,
                        "to": 10000001,
                        "price": 2000,
                        "description_vi_vn": "Bồi thường mất mát hoặc hư hỏng theo giá trị hàng hoá của bạn",
                        "description_en_us": "Coverage for loss or damage according to the value of your items"
                    },
                    {
                        "from": 10000001,
                        "to": 30000000,
                        "price": 10000,
                        "description_vi_vn": "Bồi thường mất mát hoặc hư hỏng theo giá trị hàng hoá của bạn",
                        "description_en_us": "Coverage for loss or damage according to the value of your items"
                    }
                ],
                "no_supplier_payout": True,
                "type": "COD_INSURANCE",
                "applied_stp_num": 12,
                "service_id": "SGN-BIKE",
                "description_url": "https://www.ahamove.com/tinh-nang-dam-bao-hang-hoa-100/",
                "benefit_url": "https://ahamove.com/dam-bao-don-hang-danh-cho-khach-hang/",
                "none_cod_price_blocks": {
                    "electronics": 1000,
                    "health & beauty": 1000,
                    "housing & lifestyle": 1000,
                    "food": 1000,
                    "mother & baby": 1000,
                    "fashion": 1000,
                    "grocery": 1000,
                    "restaurant": 1000,
                    "sport": 1000,
                    "drink": 1000,
                    "other": 1000,
                    "individual needs": 1000,
                    "transportation": 1000
                },
                "non_cod_description": "Bồi thường mất mát hoặc hư hỏng theo danh mục hàng hoá của bạn",
                "service_group_id": "BIKE",
                "group_id": "INSURANCE"
            },
            {
                "_id": "SGN-PARTNER-AHAMOVE-SMS",
                "name": "Gửi tin nhắn cho người nhận (BOOLEAN)",
                "enable": True,
                "support_remarks": True,
                "name_vi_vn": "Gửi tin nhắn cho người nhận (BOOLEAN)",
                "name_en_us": "Gửi tin nhắn cho người nhận (BOOLEAN)",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_d2d.png",
                "order": 1,
                "price": 1000,
                "no_supplier_payout": True,
                "type": "BOOLEAN",
                "service_id": "SGN-BIKE",
                "send_sms": True,
                "img_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_d2d.png",
                "sms_template": "Shipper AhaMove se giao don hang tu {actual_sender_name} toi quy khach trong vong {min_eta} - {max_eta} phut nua. Theo doi don hang tai: {shared_link}",
                "sms_template_v3": "Shipper AhaMove se giao don hang tu %s toi quy khach trong vong %s - %s phut nua. Theo doi don hang tai: %s",
                "description_vi_vn": "Gửi tin nhắn cho người nhận",
                "description_en_us": "Send SMS to recipient ",
                "sms_demo": "<p>Shipper AhaMove se giao don hang tu <span style=\"color: #FF8200;\"><strong>Pizza 4P's</strong></span>&nbsp;toi quy khach trong vong <span style=\"color: #FF8200;\"><strong>18 - 25&nbsp;</strong></span>phut nua. Theo doi don hang tai:&nbsp;<span style=\"color: #FF8200;\"><strong>https://track.ahamove.com/203TG2NW</strong></span></p>",
                "no_commission": False,
                "service_group_id": "BIKE"
            },
            {
                "_id": "SGN-BIKE-THERMALBAG",
                "name": "Túi giữ nhiệt",
                "enable": True,
                "name_vi_vn": "Túi giữ nhiệt",
                "name_en_us": "Thermal Bag",
                "icon_url": "https://trello-attachments.s3.amazonaws.com/5eabe9291dc6933e9e74eb2f/5f8531508904fa20c3cc89ad/1545287f04ffcc958416ab13b8bc3de5/2710.png",
                "order": 1,
                "price": 0,
                "no_commission": False,
                "description_vi_vn": "Túi giữ nhiệt",
                "description_en_us": "Thermal Bag",
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-BIKE",
                "device_types": [
                    "web",
                    "android",
                    "ios"
                ],
                "available_districts": [
                    "VN.HC.QA",
                    "VN.HC.QB",
                    "VN.HC.QC",
                    "VN.HC.QD",
                    "VN.HC.QE",
                    "VN.HC.QF",
                    "VN.HC.QG",
                    "VN.HC.QH",
                    "VN.HC.QI",
                    "VN.HC.QJ",
                    "VN.HC.QK",
                    "VN.HC.QL",
                    "VN.HC.BT",
                    "VN.HC.BH",
                    "VN.HC.GV",
                    "VN.HC.PN",
                    "VN.HC.TB",
                    "VN.HC.TP",
                    "VN.HC.TD",
                    "VN.HC.BC",
                    "VN.HC.CG",
                    "VN.HC.CC",
                    "VN.HC.HM",
                    "VN.HC.NB"
                ],
                "supplier_description_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                "supplier_description": "Giữ thức ăn bằng túi giữ nhiệt",
                "is_auto_assign_request": True,
                "is_thermal_bag_required": False,
                "service_group_id": "BIKE",
                "group_id": "THERMALBAG"
            },
            {
                "_id": "SGN-BIKE-TESTCOD",
                "name": "Bảo hiểm tự túc",
                "enable": True,
                "name_vi_vn": "Bảo hiểm tự túc",
                "name_en_us": "CBảo hiểm tự túc",
                "icon_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_cod.png",
                "img_url": "",
                "order": 1,
                "price": 0.006,
                "description_vi_vn": "Trả Bảo hiểm tự túc",
                "description_en_us": "Trả Bảo hiểm tự túc",
                "type": "COMMISSION_PERCENTAGE",
                "description": "",
                "service_id": "SGN-BIKE",
                "service_group_id": "BIKE"
            },
            {
                "_id": "SGN-BIKE-TESTPERUNIT",
                "name": "TESTPERUNIT",
                "enable": True,
                "name_vi_vn": "TEST PER UNIT",
                "name_en_us": "TEST PER UNIT",
                "icon_url": "https://s7280.pcdn.co/wp-content/uploads/2019/12/the-watermelon-effect.jpg.optimal.jpg",
                "img_url": "https://s7280.pcdn.co/wp-content/uploads/2019/12/the-watermelon-effect.jpg.optimal.jpg",
                "order": 2,
                "price": 7000,
                "min_input": 1,
                "max_input": 3,
                "description_vi_vn": "TEST PER UNIT",
                "description_en_us": "TEST PER UNIT",
                "type": "PER_UNIT",
                "description": "",
                "service_id": "SGN-BIKE",
                "service_group_id": "BIKE"
            },
            {
                "_id": "SGN-BIKE-D2D",
                "name": "Giao hàng tận tay (BOOLEAN)",
                "enable": True,
                "name_vi_vn": "Giao hàng tận tay (BOOLEAN)",
                "name_en_us": "Giao hàng tận tay (BOOLEAN)",
                "icon_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/core_services/req_d2d.png",
                "order": 3,
                "price": 10000,
                "no_commission": True,
                "type": "BOOLEAN",
                "service_id": "SGN-BIKE",
                "delivery_option": True,
                "img_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/core_services/req_d2d.png",
                "description_vi_vn": "Khách hàng có thể chọn được từng điểm giao để yêu cầu tài xế giao hàng tới tận tay người nhận.",
                "description_en_us": "Khách hàng có thể chọn được từng điểm giao để yêu cầu tài xế giao hàng tới tận tay người nhận.",
                "description_url": "https://ahamove.com/gioi-thieu-tinh-nang-giao-hang-tan-tay/",
                "supplier_description_url": "https://ahamove.com/cap-nhat-moi-tinh-nang-giao-hang-tan-tay/",
                "service_group_id": "BIKE",
                "group_id": "D2D"
            },
            {
                "_id": "SGN-BIKE-TIP",
                "name": "Hỗ trợ tài xế (PER_UNIT)",
                "enable": True,
                "name_vi_vn": "Hỗ trợ tài xế (PER_UNIT)",
                "name_en_us": "Hỗ trợ tài xế (PER_UNIT)",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/sr_tipping.png",
                "order": 4,
                "no_commission": True,
                "type": "PER_UNIT",
                "price": 5000,
                "description": "",
                "service_id": "SGN-BIKE",
                "description_vi_vn": "Hãy chọn dịch vụ này nếu bạn muốn hỗ trợ tài xế trong giờ cao điểm, khi cần giao hàng lên lầu, nơi phải tốn phí giữ xe, khi thời tiết khó khăn, hoặc đơn giản là muốn thưởng thêm cho tài xế. Ngoài ra, tính năng này sẽ giúp cho đơn hàng của bạn được ưu tiên hơn trong thời gian cao điểm.",
                "description_en_us": "This will show your support or compliment to the driver, especially in rush hours, hand to hand delivery, bad weather. Also, this feature will prioritize your request in peak time.",
                "img_url": "http://file.hstatic.net/1000010797/file/tipping_final.jpg",
                "max_input": 5,
                "no_promotion": True,
                "service_group_id": "BIKE",
                "group_id": "TIP"
            }
        ],
        "currency": "VND"
    },
    {
        "_id": "SGN-RENT-BIKE",
        "enable": True,
        "order": 1,
        "city_id": "SGN",
        "name": "Shipper riêng theo giờ",
        "rebroadcast_interval": 1200,
        "rebroadcast_limit": 1,
        "broadcast_distance": 500000,
        "complete_interval": 2,
        "name_vi_vn": "Shipper riêng theo giờ",
        "icon_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/aha-service/SieuToc.jpg",
        "map_icon_url": "https://ahamove.com/wp-content/uploads/2020/01/icon-tet.png",
        "commission_type": "PERCENTAGE",
        "commission_value": 0.212,
        "name_en_us": "Motorbike Hourly",
        "require_to": False,
        "auto_assign": False,
        "auto_assign_distance": 5000,
        "require_request": False,
        "advance_broadcast_distance": 500000,
        "timeout": 600,
        "cod": 10000000,
        "first_order_cod": 1,
        "max_stop_points": 5,
        "max_concurrent_orders": 1,
        "pending_period": 100,
        "fee_description_en_us": "Order time window:\n\nMinimal: 2 hours\nMaximal: 6 hours\nHour fee: 60.000đ/hour\nDistance limit: 12km/hour\n\nCOD operation: Still not support\n\nBooking time: 7AM - 18PM",
        "description_en_us": "Rent motor-driver hourly",
        "description_vi_vn": "Tài xế xe máy giao hàng theo giờ",
        "fee_description_vi_vn": "Thời gian đơn hàng:\n\nTối thiểu: 2 giờ \nTối đa: 6 giờ\nPhí theo giờ: 60.000đ/giờ\nGiới hạn khoảng cách: 12km/giờ\n\nỨng tiền COD: Chưa hỗ trợ\n\nThời gian đặt đơn: 7 - 18 giờ",
        "tooltips": {
            "ASSIGNING": {
                "message": [
                    "Đơn hàng của bạn đang được AhaMove xử lí. Sẽ có tài xế chấp nhận trong 5-10' tiếp theo!"
                ],
                "message_vi_vn": [
                    "Đơn hàng của bạn đang được AhaMove xử lí. Sẽ có tài xế chấp nhận trong 5-10' tiếp theo!"
                ]
            },
            "ACCEPTED": {
                "message": [
                    "Driver will arrive to your location within 15 minutes",
                    "Delivery time can take up to 2 hours"
                ],
                "message_vi_vn": [
                    "Tài xế sẽ đến chỗ bạn trong vòng 15 phút",
                    "Thời gian giao hàng có thể lên đến 2 tiếng"
                ]
            }
        },
        "supplier_description": "Giao hàng cho khách hàng cố định theo giờ",
        "notify_package_return": True,
        "cross_service": {
            "enable": False,
            "services": [],
            "non-category": []
        },
        "uniform_verify": False,
        "recommend_order": False,
        "event_callback": True,
        "uniform_verify_message_vi_vn": "Tài xế có mang đồng phục (áo, nón) hay không?",
        "uniform_verify_message_en_us": "Is your driver wearing proper uniform (including AhaMove's jacket, helmet)?",
        "recommendation_config": {
            "supplier_timeout": 3,
            "recommend_timeout": 20,
            "poolable": False,
            "recommend_radius": 700,
            "sleep_interval": 60,
            "dispatch_mode": "RECOMMEND",
            "pool_mode": "NO_POOL",
            "pool_saving_threshold": 0.2
        },
        "set_idle_status_when_creating_order": False,
        "need_confirm_before_pickup": False,
        "max_cod_per_stop_point": 10000000,
        "cod_commission": {
            "value": 0.0088,
            "none_commission_limit": 2000000
        },
        "max_cod": 10000000,
        "idle_timeout": 2,
        "delivery_type": "RENTAL",
        "cross_city": {
            "enable": False,
            "cities": [
                "SGN"
            ]
        },
        "map_icon_3d": {
            "url": "https://files.ahamove.com/sgn-bike-v4.png",
            "sprite_size": 2000,
            "sprite_count": 64
        },
        "require_pof": False,
        "enable_upload_pof": False,
        "route_api_url": "https://apistg.ahamove.com/api/v3/internal/osrm/bike/route/v1/driving/",
        "enable_platform": [
            "ahauser"
        ],
        "supplier_description_url": "https://ahamove.com/quy-trinh-giao-don-sieu-toc-sieu-re/",
        "limit_call": True,
        "group_name_en_us": "",
        "group_name_vi_vn": "",
        "same_district_delivery": False,
        "available_districts": [
            "VN.HC.BC",
            "VN.HC.CC",
            "VN.HC.CG",
            "VN.HC.HM",
            "VN.HC.NB",
            "VN.TDM",
            "VN.TA",
            "VN.HC.BH",
            "VN.HC.BT",
            "VN.HC.GV",
            "VN.HC.PN",
            "VN.HC.QJ",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.QA",
            "VN.HC.QB",
            "VN.HC.QC",
            "VN.HC.QD",
            "VN.HC.QE",
            "VN.HC.QF",
            "VN.HC.QG",
            "VN.HC.QH",
            "VN.HC.QI",
            "VN.HC.TB",
            "VN.HC.TP",
            "VN.HC.TD"
        ],
        "applied_pandemic_hours_areas": [
            "VN.HC.BC",
            "VN.HC.BH",
            "VN.HC.BT",
            "VN.HC.CG",
            "VN.HC.CC",
            "VN.HC.GV",
            "VN.HC.HM",
            "VN.HC.NB",
            "VN.HC.PN",
            "VN.HC.QA",
            "VN.HC.QJ",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.QB",
            "VN.HC.QC",
            "VN.HC.QD",
            "VN.HC.QE",
            "VN.HC.QF",
            "VN.HC.QG",
            "VN.HC.QH",
            "VN.HC.QI",
            "VN.HC.TD",
            "VN.HC.TB",
            "VN.HC.TP",
            "VN.HI.UH",
            "VN.HI.BD",
            "VN.HI.BTL",
            "VN.HI.CM",
            "VN.HI.CG",
            "VN.HI.GL",
            "VN.HI.HB",
            "VN.HI.HC",
            "VN.HI.HK",
            "VN.HI.HM",
            "VN.HI.HG",
            "VN.HI.LB",
            "VN.VC.ML",
            "VN.HI.MD",
            "VN.HI.NTL",
            "VN.HI.PX",
            "VN.HI.PT",
            "VN.HI.QO",
            "VN.HI.SS",
            "VN.HI.ST",
            "VN.HI.TO",
            "VN.HI.TT",
            "VN.HI.TX",
            "VN.HI.TN",
            "VN.HI.TC",
            "VN.HI.TH",
            "VN.HI.DP",
            "VN.HI.DA",
            "VN.HI.DD",
            "VN.HI.BV",
            "VN.BH",
            "VN.TDM",
            "VN.TA",
            "VN.DA",
            "VN.PC.BT",
            "VN.PC.NK",
            "VN.PC.CR",
            "VN.PC.VT",
            "VN.PC.PD",
            "VN.PC.TN",
            "VN.PC.TL",
            "VN.PC.CD",
            "VN.PC.OM"
        ],
        "assigning_list_order": 3,
        "same_district_delivery_areas": [
            "VN.HCM.ZONE",
            "VN.BH",
            "VN.VT.VT"
        ],
        "require_pod": False,
        "vat_rate": 0.1,
        "is_saas": False,
        "partner": False,
        "accept_message": "",
        "enable_cancellation_punishment": True,
        "priority_score": 6,
        "is_tip_allowed": False,
        "last_valid_rebroadcast_hour": 21,
        "next_valid_rebroadcast_hour": 9,
        "category": "DELIVERY",
        "opening_hours": "1-24",
        "rent_booking": {
            "instant": {
                "enable": True,
                "is_default": True,
                "limit": 5
            },
            "schedule": {
                "enable": True,
                "is_default": False,
                "limit": 10,
                "advance_book_mins": 60
            }
        },
        "rent_order_config": {
            "hide_cancel_mins": 15,
            "enable_map_mins": 15,
            "enable_contact_mins": 20,
            "extend_time": True,
            "enable_extend_mins": 20,
            "min_rent_hours": 2,
            "max_rent_hours": 6,
            "min_extend_mins": 30,
            "max_extent_mins": 120,
            "interval_step_hours": 1,
            "end_worktime": 22,
            "hide_driver_list_secs": 259200,
            "driver_checkout_mins": 5,
            "label": [
                "packaging",
                "loading"
            ]
        },
        "hour_fee": [
            {
                "from": 0,
                "to": 6,
                "base": 0,
                "price_multiplier": 70000
            },
            {
                "from": 6,
                "to": 10,
                "base": 420000,
                "price_multiplier": 70000
            }
        ],
        "valid_distance_to_perform_action": 500,
        "require_pop": True,
        "distance_fee_v3": {},
        "parent_id": "",
        "group_id": "RENT",
        "animated_url": "https://i.imgur.com/xiDxEYN.png",
        "requests": [
            {
                "_id": "SGN-RENT-BIKE-BULKY",
                "name": "Giao hàng cồng kềnh",
                "enable": True,
                "name_vi_vn": "Giao hàng công kềnh",
                "name_en_us": "Bulky packages",
                "icon_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/Special+Request/Special+Request+Icon/Bulky_packages.jpg",
                "order": 1,
                "type": "TIER",
                "service_id": "SGN-RENT-BIKE",
                "img_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/Special+Request/Special+Request+Icon/Bulky_packages.jpg",
                "description_vi_vn": "Giao hàng cồng kềnh",
                "supplier_description_url": "https://ahamove.com/giao-hang-cong-kenh",
                "support_remarks": True,
                "tier_list": [
                    {
                        "code": "TIER_1",
                        "name_vi_vn": "Tiêu chuẩn",
                        "name_en_us": "Standard",
                        "selectable": False,
                        "price": 0,
                        "price_description_vi_vn": "Miễn phí",
                        "price_description_en_us": "Free",
                        "description_vi_vn": "50x40x50:30kg",
                        "description_en_us": "50x40x50:30kg",
                        "img_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/Special+Request/Bulky+Packages/Standard.png"
                    },
                    {
                        "code": "TIER_2",
                        "name_vi_vn": "Mức 1",
                        "name_en_us": "Package 1",
                        "price": 10000,
                        "selectable": True,
                        "description_vi_vn": "60x50x60:40kg",
                        "description_en_us": "60x50x60:40kg",
                        "img_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/Special+Request/Bulky+Packages/Tier+1.png"
                    },
                    {
                        "code": "TIER_3",
                        "name_vi_vn": "Mức 2",
                        "name_en_us": "Package 2",
                        "selectable": True,
                        "price": 20000,
                        "description_vi_vn": "70x60x70:60kg",
                        "description_en_us": "70x60x70:60kg",
                        "img_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/Special+Request/Bulky+Packages/Tier+2.png"
                    },
                    {
                        "code": "TIER_4",
                        "name_vi_vn": "Mức 3",
                        "name_en_us": "Package 3",
                        "selectable": True,
                        "price": 40000,
                        "description_vi_vn": "90x70x90:80kg",
                        "description_en_us": "90x70x90:80kg",
                        "img_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/Special+Request/Bulky+Packages/Tier+3.png"
                    },
                    {
                        "code": "TIER_MAX",
                        "name_vi_vn": "Quá tải trọng",
                        "name_en_us": "Over",
                        "selectable": False,
                        "price": -1,
                        "price_description_vi_vn": "Quá tải trọng",
                        "price_description_en_us": "Overload",
                        "description_vi_vn": "90x60x90cm (100kg)",
                        "description_en_us": "90x60x90cm (100kg)",
                        "warning_message": "Hàng hoá có kích thước lớn vượt quá quy định, không cho phép vận chuyển bằng xe máy",
                        "img_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/Special+Request/Bulky+Packages/Tier+max.png"
                    }
                ],
                "service_group_id": "RENT"
            },
            {
                "_id": "SGN-RENT-BIKE-THERMALBAG",
                "name": "Túi giữ nhiệt",
                "enable": True,
                "name_vi_vn": "Túi giữ nhiệt",
                "name_en_us": "Carry parcel with thermalbag",
                "icon_url": "https://trello-attachments.s3.amazonaws.com/5eabe9291dc6933e9e74eb2f/5f8531508904fa20c3cc89ad/1545287f04ffcc958416ab13b8bc3de5/2710.png",
                "order": 3,
                "price": 15000,
                "no_commission": False,
                "type": "BOOLEAN",
                "service_id": "SGN-RENT-BIKE",
                "delivery_option": False,
                "img_url": "https://trello-attachments.s3.amazonaws.com/5eabe9291dc6933e9e74eb2f/5f8531508904fa20c3cc89ad/1545287f04ffcc958416ab13b8bc3de5/2710.png",
                "description_vi_vn": "Tìm kiếm tài xế có túi giữ nhiệt",
                "description_en_us": "Finding dedicated driver who have a thermalbag",
                "description_url": "https://ahamove.com/gioi-thieu-tinh-nang-giao-hang-tan-tay/",
                "supplier_description_url": "https://ahamove.com/cap-nhat-moi-tinh-nang-giao-hang-tan-tay/",
                "service_group_id": "RENT"
            }
        ],
        "currency": "VND"
    },
    {
        "_id": "SGN-RENT-TRUCK",
        "enable": True,
        "order": 1,
        "city_id": "SGN",
        "name": "Xe tải theo giờ",
        "rebroadcast_interval": 1200,
        "rebroadcast_limit": 1,
        "broadcast_distance": 500000,
        "complete_interval": 2,
        "name_vi_vn": "Xe tải theo giờ",
        "icon_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/aha-service/SieuToc.jpg",
        "map_icon_url": "https://ahamove.com/wp-content/uploads/2020/01/icon-tet.png",
        "commission_type": "PERCENTAGE",
        "commission_value": 0.212,
        "name_en_us": "Truck Hourly",
        "require_to": False,
        "auto_assign": False,
        "auto_assign_distance": 5000,
        "require_request": False,
        "advance_broadcast_distance": 500000,
        "timeout": 600,
        "cod": 10000000,
        "first_order_cod": 1,
        "max_stop_points": 5,
        "max_concurrent_orders": 1,
        "pending_period": 100,
        "fee_description_en_us": "Order time window:\n\nMinimal: 2 hours\nMaximal: 6 hours\nHour fee: 60.000đ/hour\nDistance limit: 12km/hour\n\nCOD operation: Still not support\n\nBooking time: 7AM - 18PM",
        "description_en_us": "Rent truck-driver hourly",
        "description_vi_vn": "Tài xế xe tải giao hàng theo giờ",
        "fee_description_vi_vn": "Thời gian đơn hàng:\n\nTối thiểu: 2 giờ \nTối đa: 6 giờ\nPhí theo giờ: 60.000đ/giờ\nGiới hạn khoảng cách: 12km/giờ\n\nỨng tiền COD: Chưa hỗ trợ\n\nThời gian đặt đơn: 7 - 18 giờ",
        "tooltips": {
            "ASSIGNING": {
                "message": [
                    "Đơn hàng của bạn đang được AhaMove xử lí. Sẽ có tài xế chấp nhận trong 5-10' tiếp theo!"
                ],
                "message_vi_vn": [
                    "Đơn hàng của bạn đang được AhaMove xử lí. Sẽ có tài xế chấp nhận trong 5-10' tiếp theo!"
                ]
            },
            "ACCEPTED": {
                "message": [
                    "Driver will arrive to your location within 15 minutes",
                    "Delivery time can take up to 2 hours"
                ],
                "message_vi_vn": [
                    "Tài xế sẽ đến chỗ bạn trong vòng 15 phút",
                    "Thời gian giao hàng có thể lên đến 2 tiếng"
                ]
            }
        },
        "supplier_description": "Giao hàng cho khách hàng cố định theo giờ",
        "notify_package_return": True,
        "cross_service": {
            "enable": False,
            "services": [],
            "non-category": []
        },
        "uniform_verify": False,
        "recommend_order": False,
        "event_callback": True,
        "uniform_verify_message_vi_vn": "Tài xế có mang đồng phục (áo, nón) hay không?",
        "uniform_verify_message_en_us": "Is your driver wearing proper uniform (including AhaMove's jacket, helmet)?",
        "recommendation_config": {
            "supplier_timeout": 3,
            "recommend_timeout": 20,
            "poolable": False,
            "recommend_radius": 700,
            "sleep_interval": 60,
            "dispatch_mode": "RECOMMEND",
            "pool_mode": "NO_POOL",
            "pool_saving_threshold": 0.2
        },
        "set_idle_status_when_creating_order": False,
        "need_confirm_before_pickup": False,
        "max_cod_per_stop_point": 10000000,
        "cod_commission": {
            "value": 0.0088,
            "none_commission_limit": 2000000
        },
        "max_cod": 10000000,
        "idle_timeout": 2,
        "delivery_type": "RENTAL",
        "cross_city": {
            "enable": False,
            "cities": [
                "SGN"
            ]
        },
        "map_icon_3d": {
            "url": "https://files.ahamove.com/sgn-bike-v4.png",
            "sprite_size": 2000,
            "sprite_count": 64
        },
        "require_pof": False,
        "enable_upload_pof": False,
        "route_api_url": "https://apistg.ahamove.com/api/v3/internal/osrm/bike/route/v1/driving/",
        "enable_platform": [
            "ahauser"
        ],
        "supplier_description_url": "https://ahamove.com/quy-trinh-giao-don-sieu-toc-sieu-re/",
        "limit_call": True,
        "group_name_en_us": "",
        "group_name_vi_vn": "",
        "same_district_delivery": False,
        "available_districts": [
            "VN.HC.NB",
            "VN.HC.CG",
            "VN.HC.CC",
            "VN.HC.BC",
            "VN.HC.HM",
            "VN.TDM",
            "VN.TA",
            "VN.DA",
            "VN.HC.QB",
            "VN.HC.QC",
            "VN.HC.QG",
            "VN.HC.BH",
            "VN.HC.GV",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.PN",
            "VN.HC.QJ",
            "VN.HC.QD",
            "VN.HC.BT",
            "VN.HC.QF",
            "VN.HC.QA",
            "VN.HC.QE",
            "VN.HC.TB",
            "VN.HC.TD",
            "VN.HC.QH",
            "VN.HC.QI",
            "VN.HC.TP"
        ],
        "applied_pandemic_hours_areas": [
            "VN.HC.BC",
            "VN.HC.BH",
            "VN.HC.BT",
            "VN.HC.CG",
            "VN.HC.CC",
            "VN.HC.GV",
            "VN.HC.HM",
            "VN.HC.NB",
            "VN.HC.PN",
            "VN.HC.QA",
            "VN.HC.QJ",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.QB",
            "VN.HC.QC",
            "VN.HC.QD",
            "VN.HC.QE",
            "VN.HC.QF",
            "VN.HC.QG",
            "VN.HC.QH",
            "VN.HC.QI",
            "VN.HC.TD",
            "VN.HC.TB",
            "VN.HC.TP",
            "VN.HI.UH",
            "VN.HI.BD",
            "VN.HI.BTL",
            "VN.HI.CM",
            "VN.HI.CG",
            "VN.HI.GL",
            "VN.HI.HB",
            "VN.HI.HC",
            "VN.HI.HK",
            "VN.HI.HM",
            "VN.HI.HG",
            "VN.HI.LB",
            "VN.VC.ML",
            "VN.HI.MD",
            "VN.HI.NTL",
            "VN.HI.PX",
            "VN.HI.PT",
            "VN.HI.QO",
            "VN.HI.SS",
            "VN.HI.ST",
            "VN.HI.TO",
            "VN.HI.TT",
            "VN.HI.TX",
            "VN.HI.TN",
            "VN.HI.TC",
            "VN.HI.TH",
            "VN.HI.DP",
            "VN.HI.DA",
            "VN.HI.DD",
            "VN.HI.BV",
            "VN.BH",
            "VN.TDM",
            "VN.TA",
            "VN.DA",
            "VN.PC.BT",
            "VN.PC.NK",
            "VN.PC.CR",
            "VN.PC.VT",
            "VN.PC.PD",
            "VN.PC.TN",
            "VN.PC.TL",
            "VN.PC.CD",
            "VN.PC.OM"
        ],
        "assigning_list_order": 3,
        "same_district_delivery_areas": [
            "VN.HCM.ZONE",
            "VN.BH",
            "VN.VT.VT"
        ],
        "require_pod": False,
        "vat_rate": 0.1,
        "is_saas": False,
        "partner": False,
        "accept_message": "",
        "enable_cancellation_punishment": True,
        "priority_score": 6,
        "is_tip_allowed": False,
        "last_valid_rebroadcast_hour": 21,
        "next_valid_rebroadcast_hour": 9,
        "category": "RENTAL",
        "opening_hours": "7-24",
        "rent_booking": {
            "instant": {
                "enable": True,
                "is_default": True,
                "limit": 5
            },
            "schedule": {
                "enable": True,
                "is_default": False,
                "limit": 10,
                "advance_book_mins": 60
            }
        },
        "rent_order_config": {
            "hide_cancel_mins": 15,
            "enable_map_mins": 15,
            "enable_contact_mins": 20,
            "extend_time": True,
            "enable_extend_mins": 20,
            "min_rent_hours": 2,
            "max_rent_hours": 6,
            "min_extend_mins": 30,
            "max_extent_mins": 120,
            "interval_step_hours": 1,
            "end_worktime": 22,
            "hide_driver_list_secs": 259200,
            "driver_checkout_mins": 5,
            "label": [
                "packaging",
                "loading"
            ]
        },
        "hour_fee": [
            {
                "from": 0,
                "to": 6,
                "base": 0,
                "price_multiplier": 70000
            },
            {
                "from": 6,
                "to": 10,
                "base": 420000,
                "price_multiplier": 70000
            }
        ],
        "valid_distance_to_perform_action": 500,
        "require_pop": True,
        "distance_fee_v3": {},
        "group_id": "RENT",
        "animated_url": "https://i.imgur.com/xiDxEYN.png",
        "requests": [],
        "currency": "VND"
    },
    {
        "_id": "SGN-RENTAL-BIKE",
        "enable": True,
        "order": 1,
        "city_id": "SGN",
        "name": "Shipper riêng theo giờ",
        "rebroadcast_interval": 1200,
        "rebroadcast_limit": 1,
        "broadcast_distance": 500000,
        "complete_interval": 2,
        "name_vi_vn": "Shipper riêng theo giờ",
        "icon_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/aha-service/SieuToc.jpg",
        "map_icon_url": "https://ahamove.com/wp-content/uploads/2020/01/icon-tet.png",
        "commission_type": "PERCENTAGE",
        "commission_value": 0.212,
        "name_en_us": "Motorbike Hourly",
        "require_to": False,
        "auto_assign": False,
        "auto_assign_distance": 5000,
        "require_request": False,
        "advance_broadcast_distance": 500000,
        "timeout": 600,
        "cod": 10000000,
        "first_order_cod": 1,
        "max_stop_points": 5,
        "max_concurrent_orders": 1,
        "pending_period": 100,
        "fee_description_en_us": "Order time window:\n\nMinimal: 2 hours\nMaximal: 6 hours\nHour fee: 60.000đ/hour\nDistance limit: 12km/hour\n\nCOD operation: Still not support\n\nBooking time: 7AM - 18PM",
        "description_en_us": " motor-driver hourly",
        "description_vi_vn": "Tài xế xe máy giao hàng theo giờ",
        "fee_description_vi_vn": "Thời gian đơn hàng:\n\nTối thiểu: 2 giờ \nTối đa: 6 giờ\nPhí theo giờ: 60.000đ/giờ\nGiới hạn khoảng cách: 12km/giờ\n\nỨng tiền COD: Chưa hỗ trợ\n\nThời gian đặt đơn: 7 - 18 giờ",
        "tooltips": {
            "ASSIGNING": {
                "message": [
                    "Đơn hàng của bạn đang được AhaMove xử lí. Sẽ có tài xế chấp nhận trong 5-10' tiếp theo!"
                ],
                "message_vi_vn": [
                    "Đơn hàng của bạn đang được AhaMove xử lí. Sẽ có tài xế chấp nhận trong 5-10' tiếp theo!"
                ]
            },
            "ACCEPTED": {
                "message": [
                    "Driver will arrive to your location within 15 minutes",
                    "Delivery time can take up to 2 hours"
                ],
                "message_vi_vn": [
                    "Tài xế sẽ đến chỗ bạn trong vòng 15 phút",
                    "Thời gian giao hàng có thể lên đến 2 tiếng"
                ]
            }
        },
        "supplier_description": "Giao hàng cho khách hàng cố định theo giờ",
        "notify_package_return": True,
        "cross_service": {
            "enable": False,
            "services": [],
            "non-category": []
        },
        "uniform_verify": False,
        "recommend_order": False,
        "event_callback": True,
        "uniform_verify_message_vi_vn": "Tài xế có mang đồng phục (áo, nón) hay không?",
        "uniform_verify_message_en_us": "Is your driver wearing proper uniform (including AhaMove's jacket, helmet)?",
        "recommendation_config": {
            "supplier_timeout": 10,
            "recommend_timeout": 20,
            "poolable": False,
            "recommend_radius": 700,
            "sleep_interval": 60,
            "dispatch_mode": "RECOMMEND",
            "pool_mode": "NO_POOL",
            "pool_saving_threshold": 0.2
        },
        "set_idle_status_when_creating_order": False,
        "need_confirm_before_pickup": False,
        "max_cod_per_stop_point": 10000000,
        "cod_commission": {
            "value": 0.0088,
            "none_commission_limit": 2000000
        },
        "max_cod": 10000000,
        "idle_timeout": 2,
        "cross_city": {
            "enable": False,
            "cities": [
                "SGN"
            ]
        },
        "map_icon_3d": {
            "url": "https://files.ahamove.com/sgn-bike-v4.png",
            "sprite_size": 2000,
            "sprite_count": 64
        },
        "require_pof": False,
        "enable_upload_pof": False,
        "route_api_url": "https://apistg.ahamove.com/api/v3/internal/osrm/bike/route/v1/driving/",
        "enable_platform": [
            "ahauser"
        ],
        "supplier_description_url": "https://ahamove.com/quy-trinh-giao-don-sieu-toc-sieu-re/",
        "limit_call": True,
        "group_name_en_us": "",
        "group_name_vi_vn": "",
        "same_district_delivery": False,
        "available_districts": [
            "VN.HC.BC",
            "VN.HC.CC",
            "VN.HC.CG",
            "VN.HC.HM",
            "VN.HC.NB",
            "VN.TDM",
            "VN.TA",
            "VN.HC.BH",
            "VN.HC.BT",
            "VN.HC.GV",
            "VN.HC.PN",
            "VN.HC.QJ",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.QA",
            "VN.HC.QB",
            "VN.HC.QC",
            "VN.HC.QD",
            "VN.HC.QE",
            "VN.HC.QF",
            "VN.HC.QG",
            "VN.HC.QH",
            "VN.HC.QI",
            "VN.HC.TB",
            "VN.HC.TP",
            "VN.HC.TD"
        ],
        "applied_pandemic_hours_areas": [
            "VN.HC.BC",
            "VN.HC.BH",
            "VN.HC.BT",
            "VN.HC.CG",
            "VN.HC.CC",
            "VN.HC.GV",
            "VN.HC.HM",
            "VN.HC.NB",
            "VN.HC.PN",
            "VN.HC.QA",
            "VN.HC.QJ",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.QB",
            "VN.HC.QC",
            "VN.HC.QD",
            "VN.HC.QE",
            "VN.HC.QF",
            "VN.HC.QG",
            "VN.HC.QH",
            "VN.HC.QI",
            "VN.HC.TD",
            "VN.HC.TB",
            "VN.HC.TP",
            "VN.HI.UH",
            "VN.HI.BD",
            "VN.HI.BTL",
            "VN.HI.CM",
            "VN.HI.CG",
            "VN.HI.GL",
            "VN.HI.HB",
            "VN.HI.HC",
            "VN.HI.HK",
            "VN.HI.HM",
            "VN.HI.HG",
            "VN.HI.LB",
            "VN.VC.ML",
            "VN.HI.MD",
            "VN.HI.NTL",
            "VN.HI.PX",
            "VN.HI.PT",
            "VN.HI.QO",
            "VN.HI.SS",
            "VN.HI.ST",
            "VN.HI.TO",
            "VN.HI.TT",
            "VN.HI.TX",
            "VN.HI.TN",
            "VN.HI.TC",
            "VN.HI.TH",
            "VN.HI.DP",
            "VN.HI.DA",
            "VN.HI.DD",
            "VN.HI.BV",
            "VN.BH",
            "VN.TDM",
            "VN.TA",
            "VN.DA",
            "VN.PC.BT",
            "VN.PC.NK",
            "VN.PC.CR",
            "VN.PC.VT",
            "VN.PC.PD",
            "VN.PC.TN",
            "VN.PC.TL",
            "VN.PC.CD",
            "VN.PC.OM"
        ],
        "assigning_list_order": 3,
        "same_district_delivery_areas": [
            "VN.HCM.ZONE",
            "VN.BH",
            "VN.VT.VT"
        ],
        "require_pod": False,
        "vat_rate": 0.1,
        "is_saas": False,
        "partner": False,
        "accept_message": "",
        "enable_cancellation_punishment": True,
        "priority_score": 6,
        "is_tip_allowed": False,
        "last_valid_rebroadcast_hour": 21,
        "next_valid_rebroadcast_hour": 9,
        "opening_hours": "1-24",
        "valid_distance_to_perform_action": 500,
        "require_pop": True,
        "distance_fee_v3": {},
        "parent_id": "",
        "hour_fee": [],
        "animated_url": "https://i.imgur.com/xiDxEYN.png",
        "requests": [],
        "currency": "VND"
    },
    {
        "_id": "SGN-EV",
        "enable": True,
        "order": 1,
        "city_id": "SGN",
        "name": "Siêu Tốc Xe Điện",
        "rebroadcast_interval": 1200,
        "rebroadcast_limit": 2,
        "broadcast_distance": 500000,
        "complete_interval": 2,
        "name_vi_vn": "Siêu Tốc Xe Điện",
        "icon_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/aha-service/SieuToc.jpg",
        "map_icon_url": "https://ahamove.com/wp-content/uploads/2020/01/icon-tet.png",
        "distance_fee": "(25000 if x <= 4 else 25000 + (x - 4) * 5500)",
        "commission_type": "PERCENTAGE",
        "commission_value": 0.212,
        "max_distance": 100000,
        "stop_fee": 5500,
        "name_en_us": "Siêu Tốc Xe Điện",
        "require_to": True,
        "name_vi_VN": "Siêu Tốc",
        "auto_assign": False,
        "auto_assign_distance": 5000,
        "require_request": False,
        "advance_broadcast_distance": 500000,
        "timeout": 600,
        "cod": 10000000,
        "first_order_cod": 1,
        "max_stop_points": 5,
        "max_concurrent_orders": 1,
        "pending_period": 100,
        "fee_description_en_us": "Thời gian: tối đa 1 giờ (áp dụng với đơn hàng dưới 6km)\n\nSố điểm giao hàng tối đa: 5\n\nPhí mỗi điểm giao thêm: 5,000đ\nKhu vực giao: Giao liên quận\n\nPhí quãng đường:\n- 4 km đầu: 23,000đ\n- Trên 4 km: 5,000đ/km\n\nMức COD tối đa: 10,000,000đ\nPhí COD:\n- COD < 2,000,000đ: miễn phí\n- COD >= 2,000,000đ: 0,8% x Giá trị COD",
        "description_en_us": "Deliver within an hour",
        "description_vi_vn": "Giao hàng trong 1h",
        "fee_description_vi_vn": "Thời gian: tối đa 1 giờ (áp dụng với đơn hàng dưới 6km)\n\nSố điểm giao hàng tối đa: 5\n\nPhí mỗi điểm giao thêm: 5,000đ\nKhu vực giao: Giao liên quận\n\nPhí quãng đường:\n- 4 km đầu: 23,000đ\n- Trên 4 km: 5,000đ/km\n\nMức COD tối đa: 10,000,000đ\nPhí COD:\n- COD < 2,000,000đ: miễn phí\n- COD >= 2,000,000đ: 0,8% x Giá trị COD",
        "tooltips": {
            "ASSIGNING": {
                "message": [
                    "Đơn hàng của bạn đang được AhaMove xử lí. Sẽ có tài xế chấp nhận trong 5-10' tiếp theo!"
                ],
                "message_vi_vn": [
                    "Đơn hàng của bạn đang được AhaMove xử lí. Sẽ có tài xế chấp nhận trong 5-10' tiếp theo!"
                ]
            },
            "ACCEPTED": {
                "message": [
                    "Driver will arrive to your location within 15 minutes",
                    "Delivery time can take up to 2 hours"
                ],
                "message_vi_vn": [
                    "Tài xế sẽ đến chỗ bạn trong vòng 15 phút",
                    "Thời gian giao hàng có thể lên đến 2 tiếng"
                ]
            }
        },
        "parent_id": "SGN-GROUP-BIKE_EXPRESS",
        "supplier_description": "Giao hoả tốc trong 1h",
        "notify_package_return": True,
        "cross_service": {
            "enable": True,
            "services": [],
            "non-category": [
                "Corporation - Cake",
                "Corporation - Dry food"
            ]
        },
        "uniform_verify": True,
        "recommend_order": False,
        "event_callback": True,
        "uniform_verify_message_vi_vn": "Tài xế có mang đồng phục (áo, nón) hay không?",
        "uniform_verify_message_en_us": "Is your driver wearing proper uniform (including AhaMove's jacket, helmet)?",
        "recommendation_config": {
            "supplier_timeout": 20,
            "recommend_timeout": 20,
            "poolable": False,
            "recommend_radius": 700,
            "sleep_interval": 60,
            "dispatch_mode": "RECOMMEND",
            "pool_mode": "NO_POOL",
            "pool_saving_threshold": 0.2
        },
        "set_idle_status_when_creating_order": False,
        "need_confirm_before_pickup": False,
        "service_description_vi_vn": {
            "fee_desc": {
                "0-4km": 23000,
                "Mỗi km tiếp theo": 5000
            },
            "sla": {
                "COD tối đa": 500000,
                "Trọng lượng tối đa": "5kg",
                "Kích thước tối đa": "25(D) x 32(R) x 12(C) cm"
            },
            "more_details": [
                "Giá đã bao gồm VAT",
                "Nếu giao đồ ăn, xin vui lòng cân nhắc thời gian giao hàng"
            ]
        },
        "note": "1. Vui lòng gọi điện cho người nhận trước khi đến lấy hàng.\n2. Đơn hàng không cần ứng tiền COD, vẫn thu tiền COD từ người nhận và nộp lại qua MoMo/Tk Ahamove.\n3. Tài xế huỷ đơn thì phải gọi lên tổng đài. Tuyệt đối không lấy hàng đi nếu chưa gọi được cho người nhận.\n4. Olala.\n5. Olele.",
        "max_cod_per_stop_point": 1300000,
        "cod_commission": {
            "value": 0.0088,
            "none_commission_limit": 2000000
        },
        "max_cod": 10000000,
        "idle_timeout": 2,
        "committed_time_formula": "if ( x <= 6 ) {60} else {((x -6) * 5 + 60)}",
        "delivery_type": "INSTANT",
        "cross_city": {
            "enable": False,
            "cities": [
                "SGN"
            ]
        },
        "map_icon_3d": {
            "url": "https://files.ahamove.com/sgn-bike-v4.png",
            "sprite_size": 2000,
            "sprite_count": 64
        },
        "require_pof": True,
        "enable_upload_pof": True,
        "route_api_url": "https://apistg.ahamove.com/api/v3/internal/osrm/bike/route/v1/driving/",
        "enable_platform": [
            "momo_deeplink",
            "momo_permission",
            "zalo",
            "zalopay",
            "smartpay_deeplink",
            "viettel-pay_deeplink",
            "shopee-pay_deeplink",
            "onwheel",
            "vpbank_deeplink"
        ],
        "supplier_description_url": "https://ahamove.com/quy-trinh-giao-don-sieu-toc-sieu-re/",
        "limit_call": True,
        "distance_fee_v3": {
            "blocks": [
                {
                    "from": 0,
                    "to": 4,
                    "base": 25000,
                    "price_multiplier": 0
                },
                {
                    "from": 4,
                    "to": 100000,
                    "base": 25000,
                    "price_multiplier": 5500
                }
            ],
            "hour_rates": []
        },
        "group_name_en_us": "Fast delivery",
        "group_name_vi_vn": "Giao nhanh",
        "same_district_delivery": False,
        "available_districts": [
            "VN.HC.BC",
            "VN.HC.CC",
            "VN.HC.CG",
            "VN.HC.HM",
            "VN.HC.NB",
            "VN.TDM",
            "VN.BH",
            "VN.LT",
            "VN.TA",
            "VN.DA",
            "VN.HC.BH",
            "VN.HC.BT",
            "VN.HC.GV",
            "VN.HC.PN",
            "VN.HC.QJ",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.QA",
            "VN.HC.QB",
            "VN.HC.QC",
            "VN.HC.QD",
            "VN.HC.QE",
            "VN.HC.QF",
            "VN.HC.QG",
            "VN.HC.QH",
            "VN.HC.QI",
            "VN.HC.TB",
            "VN.HC.TP",
            "VN.HC.TD"
        ],
        "applied_pandemic_hours_areas": [
            "VN.HC.BC",
            "VN.HC.BH",
            "VN.HC.BT",
            "VN.HC.CG",
            "VN.HC.CC",
            "VN.HC.GV",
            "VN.HC.HM",
            "VN.HC.NB",
            "VN.HC.PN",
            "VN.HC.QA",
            "VN.HC.QJ",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.QB",
            "VN.HC.QC",
            "VN.HC.QD",
            "VN.HC.QE",
            "VN.HC.QF",
            "VN.HC.QG",
            "VN.HC.QH",
            "VN.HC.QI",
            "VN.HC.TD",
            "VN.HC.TB",
            "VN.HC.TP",
            "VN.HI.UH",
            "VN.HI.BD",
            "VN.HI.BTL",
            "VN.HI.CM",
            "VN.HI.CG",
            "VN.HI.GL",
            "VN.HI.HB",
            "VN.HI.HC",
            "VN.HI.HK",
            "VN.HI.HM",
            "VN.HI.HG",
            "VN.HI.LB",
            "VN.VC.ML",
            "VN.HI.MD",
            "VN.HI.NTL",
            "VN.HI.PX",
            "VN.HI.PT",
            "VN.HI.QO",
            "VN.HI.SS",
            "VN.HI.ST",
            "VN.HI.TO",
            "VN.HI.TT",
            "VN.HI.TX",
            "VN.HI.TN",
            "VN.HI.TC",
            "VN.HI.TH",
            "VN.HI.DP",
            "VN.HI.DA",
            "VN.HI.DD",
            "VN.HI.BV",
            "VN.BH",
            "VN.TDM",
            "VN.TA",
            "VN.DA",
            "VN.PC.BT",
            "VN.PC.NK",
            "VN.PC.CR",
            "VN.PC.VT",
            "VN.PC.PD",
            "VN.PC.TN",
            "VN.PC.TL",
            "VN.PC.CD",
            "VN.PC.OM"
        ],
        "assigning_list_order": 3,
        "same_district_delivery_areas": [
            "VN.HCM.ZONE",
            "VN.BH",
            "VN.VT.VT"
        ],
        "require_pod": True,
        "vat_rate": 0.1,
        "is_saas": False,
        "partner": False,
        "accept_message": "",
        "enable_cancellation_punishment": True,
        "priority_score": 2,
        "is_tip_allowed": True,
        "last_valid_rebroadcast_hour": 9,
        "next_valid_rebroadcast_hour": 10,
        "require_pop": False,
        "assigning_before_bk": [
            {
                "from": 0,
                "to": 18,
                "value": 3600
            },
            {
                "from": 16,
                "to": 20,
                "value": 600
            },
            {
                "from": 20,
                "to": 24,
                "value": 1800
            }
        ],
        "group_id": "BIKE",
        "animated_url": "https://i.imgur.com/xiDxEYN.png",
        "requests": [],
        "currency": "VND"
    },
    {
        "_id": "SGN-AHA-RIDE",
        "enable": True,
        "order": 1,
        "city_id": "SGN",
        "name": "AhaRide",
        "rebroadcast_interval": 1200,
        "rebroadcast_limit": 2,
        "broadcast_distance": 500000,
        "complete_interval": 2,
        "name_vi_vn": "Siêu TốcC",
        "icon_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/aha-service/SieuToc.jpg",
        "map_icon_url": "https://ahamove.com/wp-content/uploads/2020/01/icon-tet.png",
        "distance_fee": "(25000 if x <= 4 else 25000 + (x - 4) * 5500)",
        "commission_type": "PERCENTAGE",
        "commission_value": 0.212,
        "max_distance": 100000,
        "stop_fee": 5500,
        "name_en_us": "AhaRide",
        "require_to": True,
        "name_vi_VN": "AhaRide",
        "auto_assign": False,
        "auto_assign_distance": 5000,
        "require_request": False,
        "advance_broadcast_distance": 500000,
        "timeout": 600,
        "cod": 10000000,
        "first_order_cod": 1,
        "max_stop_points": 5,
        "max_concurrent_orders": 1,
        "pending_period": 100,
        "fee_description_en_us": "Thời gian: tối đa 1 giờ (áp dụng với đơn hàng dưới 6km)\n\nSố điểm giao hàng tối đa: 5\n\nPhí mỗi điểm giao thêm: 5,000đ\nKhu vực giao: Giao liên quận\n\nPhí quãng đường:\n- 4 km đầu: 23,000đ\n- Trên 4 km: 5,000đ/km\n\nMức COD tối đa: 10,000,000đ\nPhí COD:\n- COD < 2,000,000đ: miễn phí\n- COD >= 2,000,000đ: 0,8% x Giá trị COD",
        "description_en_us": "Deliver within an hour",
        "description_vi_vn": "Giao hàng trong 1h",
        "fee_description_vi_vn": "Thời gian: tối đa 1 giờ (áp dụng với đơn hàng dưới 6km)\n\nSố điểm giao hàng tối đa: 5\n\nPhí mỗi điểm giao thêm: 5,000đ\nKhu vực giao: Giao liên quận\n\nPhí quãng đường:\n- 4 km đầu: 23,000đ\n- Trên 4 km: 5,000đ/km\n\nMức COD tối đa: 10,000,000đ\nPhí COD:\n- COD < 2,000,000đ: miễn phí\n- COD >= 2,000,000đ: 0,8% x Giá trị COD",
        "tooltips": {
            "ASSIGNING": {
                "message": [
                    "Đơn hàng của bạn đang được AhaMove xử lí. Sẽ có tài xế chấp nhận trong 5-10' tiếp theo!"
                ],
                "message_vi_vn": [
                    "Đơn hàng của bạn đang được AhaMove xử lí. Sẽ có tài xế chấp nhận trong 5-10' tiếp theo!"
                ]
            },
            "ACCEPTED": {
                "message": [
                    "Driver will arrive to your location within 15 minutes",
                    "Delivery time can take up to 2 hours"
                ],
                "message_vi_vn": [
                    "Tài xế sẽ đến chỗ bạn trong vòng 15 phút",
                    "Thời gian giao hàng có thể lên đến 2 tiếng"
                ]
            }
        },
        "parent_id": "SGN-GROUP-BIKE_EXPRESS",
        "supplier_description": "Giao hoả tốc trong 1h",
        "notify_package_return": True,
        "cross_service": {
            "enable": True,
            "services": [],
            "non-category": [
                "Corporation - Cake",
                "Corporation - Dry food"
            ]
        },
        "uniform_verify": True,
        "recommend_order": False,
        "event_callback": True,
        "uniform_verify_message_vi_vn": "Tài xế có mang đồng phục (áo, nón) hay không?",
        "uniform_verify_message_en_us": "Is your driver wearing proper uniform (including AhaMove's jacket, helmet)?",
        "recommendation_config": {
            "supplier_timeout": 20,
            "recommend_timeout": 20,
            "poolable": False,
            "recommend_radius": 700,
            "sleep_interval": 60,
            "dispatch_mode": "RECOMMEND",
            "pool_mode": "NO_POOL",
            "pool_saving_threshold": 0.2
        },
        "set_idle_status_when_creating_order": False,
        "need_confirm_before_pickup": False,
        "service_description_vi_vn": {
            "fee_desc": {
                "0-4km": 23000,
                "Mỗi km tiếp theo": 5000
            },
            "sla": {
                "COD tối đa": 500000,
                "Trọng lượng tối đa": "5kg",
                "Kích thước tối đa": "25(D) x 32(R) x 12(C) cm"
            },
            "more_details": [
                "Giá đã bao gồm VAT",
                "Nếu giao đồ ăn, xin vui lòng cân nhắc thời gian giao hàng"
            ]
        },
        "note": "1. Vui lòng gọi điện cho người nhận trước khi đến lấy hàng.\n2. Đơn hàng không cần ứng tiền COD, vẫn thu tiền COD từ người nhận và nộp lại qua MoMo/Tk Ahamove.\n3. Tài xế huỷ đơn thì phải gọi lên tổng đài. Tuyệt đối không lấy hàng đi nếu chưa gọi được cho người nhận.\n4. Olala.\n5. Olele.",
        "max_cod_per_stop_point": 1300000,
        "cod_commission": {
            "value": 0.0088,
            "none_commission_limit": 2000000
        },
        "max_cod": 10000001,
        "idle_timeout": 2,
        "committed_time_formula": "if ( x <= 6 ) {60} else {((x -6) * 5 + 60)}",
        "delivery_type": "RIDE",
        "cross_city": {
            "enable": False,
            "cities": [
                "SGN"
            ]
        },
        "map_icon_3d": {
            "url": "https://files.ahamove.com/sgn-bike-v4.png",
            "sprite_size": 2000,
            "sprite_count": 64
        },
        "require_pof": True,
        "enable_upload_pof": True,
        "route_api_url": "https://apistg.ahamove.com/api/v3/internal/osrm/bike/route/v1/driving/",
        "enable_platform": [
            "momo_deeplink",
            "momo_permission",
            "zalo",
            "zalopay",
            "smartpay_deeplink",
            "viettel-pay_deeplink",
            "shopee-pay_deeplink",
            "onwheel",
            "vpbank_deeplink"
        ],
        "supplier_description_url": "https://ahamove.com/quy-trinh-giao-don-sieu-toc-sieu-re/",
        "limit_call": True,
        "distance_fee_v3": {
            "blocks": [
                {
                    "from": 0,
                    "to": 4,
                    "base": 25000,
                    "price_multiplier": 0
                },
                {
                    "from": 4,
                    "to": 100000,
                    "base": 25000,
                    "price_multiplier": 5500
                }
            ],
            "hour_rates": []
        },
        "group_name_en_us": "Fast delivery",
        "group_name_vi_vn": "Giao nhanh",
        "same_district_delivery": False,
        "assigning_list_order": 3,
        "require_pod": True,
        "vat_rate": 0.1,
        "is_saas": False,
        "partner": False,
        "accept_message": "",
        "enable_cancellation_punishment": True,
        "priority_score": 2,
        "is_tip_allowed": True,
        "last_valid_rebroadcast_hour": 9,
        "next_valid_rebroadcast_hour": 10,
        "require_pop": False,
        "est_travel_time_fee": [
            {
                "from": 0,
                "to": 1440,
                "base": 0,
                "price_multiplier": 500
            }
        ],
        "animated_url": "https://i.imgur.com/xiDxEYN.png",
        "requests": [],
        "currency": "VND"
    },
    {
        "_id": "SGN-EXPRESS",
        "commission_type": "PERCENTAGE",
        "require_to": True,
        "require_request": False,
        "notify_package_return": True,
        "cross_service": {
            "enable": True,
            "services": [
                "SGN-BIKE",
                "SGN-FOOD",
                "SGN-EXPRESS",
                "SGN-GOSHOP",
                "SGN-BIKE-INTRADISTRICT"
            ]
        },
        "cross_city": {
            "enable": True,
            "cities": [
                "SGN"
            ]
        },
        "parent_id": "",
        "committed_time_formula": "if ( x <= 2) {20} else if (x <= 6) {45} else {75}",
        "city_id": "SGN",
        "uniform_verify": False,
        "enable": True,
        "name": "Siêu Tốc - Đồ Ăn",
        "name_vi_vn": "Siêu Tốc - Đồ Ăn",
        "name_en_us": "Siêu Tốc - Đồ Ăn",
        "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/services/iconfood.png",
        "map_icon_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/core_services/xe1-02.png",
        "order": 2,
        "broadcast_distance": 2000,
        "advance_broadcast_distance": 2000,
        "stop_fee": 5000,
        "pending_period": 180,
        "timeout": 1800,
        "rebroadcast_interval": 1200,
        "max_concurrent_orders": 1,
        "max_stop_points": 2,
        "cod": 10000000,
        "max_cod": 10000000,
        "first_order_cod": 1,
        "distance_fee": "(20000 if x <= 3 else 20000 + (x - 3) * 5500)",
        "commission_value": 0.212,
        "cod_commission": {
            "value": 0.0088,
            "none_commission_limit": 1000000
        },
        "fee_description_en_us": "Leadtime: Maximum 30min\n(distance under 5km)\n\nMaximum drop off: 1\n\n\n\nDistance fee:\n- First 3 km: 20,000 VND\n- Over 3 km: 5,500 VND/km\n\nPayload capacity: 10kg\nSuitable goods (LxWxH): 50x40x50 cm\n\n\nMaximum COD: 10,000,000 VND \nCOD fee:\n- COD < 2,000,000 VND: Free\n- COD >= 2,000,000 VND: 0.88% * Value of COD",
        "description_en_us": "Giao siêu nhanh chỉ 30 phút",
        "description_vi_vn": "Giao siêu nhanh chỉ 30 phút",
        "fee_description_vi_vn": "Thời gian: tối đa 30 phút (áp dụng đơn\n hàng dưới 5km)\n\nSố điểm giao tối đa: 1\n\nPhí quãng đường:\n- 3km đầu: 20,000đ\n- Trên 3km: 5,500đ/km\n\nTrọng lượng tiêu chuẩn: 10kg\nKích thước tiêu chuẩn: 50x40x50\n\nMức COD tối đa: 10,000,000đ\nPhí COD:\n- COD < 1,000,000đ: Miễn phí\n- COD >= 1,000,000đ: 0.88%*giá trị COD",
        "delay_time": 3,
        "available_districts": [
            "VN.HC.BC",
            "VN.HC.CC",
            "VN.HC.CG",
            "VN.HC.HM",
            "VN.HC.NB",
            "VN.HC.BH",
            "VN.HC.BT",
            "VN.HC.GV",
            "VN.HC.PN",
            "VN.HC.QJ",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.QA",
            "VN.HC.QB",
            "VN.HC.QC",
            "VN.HC.QD",
            "VN.HC.QE",
            "VN.HC.QF",
            "VN.HC.QG",
            "VN.HC.QH",
            "VN.HC.QI",
            "VN.HC.TB",
            "VN.HC.TP",
            "VN.HC.TD"
        ],
        "delivery_type": "INSTANT",
        "payment_method": [
            {
                "description": "Cash",
                "description_vi_vn": "Tiền mặt",
                "payment": "cash",
                "order": 1
            },
            {
                "description": "Balance",
                "description_vi_vn": "Ví AhaMove",
                "payment": "balance",
                "order": 2
            },
            {
                "description": "MoMo e-Wallet",
                "description_vi_vn": "Ví điện tử MoMo",
                "payment": "momo",
                "order": 3
            },
            {
                "description": "ZaloPay e-Wallet",
                "description_vi_vn": "Ví điện tử ZaloPay",
                "payment": "Zalopay",
                "order": 4
            }
        ],
        "enable_platform": [
            "momo_deeplink",
            "momo_permission",
            "zalo",
            "zalopay",
            "smartpay_deeplink",
            "shopee-pay_deeplink"
        ],
        "same_district_delivery": False,
        "advance_max_concurrent_orders": 1,
        "same_district_delivery_areas": [
            "VN.HCM.ZONE"
        ],
        "applied_pandemic_hours_areas": [
            "VN.BH",
            "VN.PC.BT",
            "VN.PC.NK",
            "VN.PC.CR",
            "VN.PC.VT",
            "VN.PC.PD",
            "VN.PC.TN",
            "VN.PC.TL",
            "VN.PC.CD",
            "VN.PC.OM"
        ],
        "assigning_list_order": 3,
        "supplier_description_vi_vn": "Dịch vụ Siêu tốc - Đồ ăn được thực hiện trong vòng 30 phút, được nhận tối đa 1 đơn",
        "group_name_en_us": "Giao nhanh",
        "group_name_vi_vn": "Giao nhanh",
        "recommendation_config": {
            "supplier_timeout": 20,
            "recommend_timeout": 60,
            "recommend_radius": 1000,
            "sleep_interval": 60,
            "dispatch_mode": "RECOMMEND",
            "pool_mode": "NO_POOL",
            "pool_saving_threshold": 0.2,
            "poolable": False
        },
        "supplier_description": "Dịch vụ Siêu tốc - Đồ ăn được thực hiện trong vòng 30 phút, được nhận tối đa 1 đơn",
        "supplier_description_url": "https://ahamove.com/quy-trinh-giao-hang-dich-vu-co-ban",
        "distance_fee_v3": {
            "blocks": [
                {
                    "from": 0,
                    "to": 3,
                    "base": 20000,
                    "price_multiplier": 0
                },
                {
                    "from": 3,
                    "to": 100000,
                    "base": 20000,
                    "price_multiplier": 5500
                }
            ],
            "hour_rates": []
        },
        "vat_rate": 0.1,
        "priority_score": 3,
        "is_pay_cod_discrepancy": True,
        "route_api_url": "https://apistg.ahamove.com/api/v3/internal/osrm/bike/route/v1/driving/",
        "route_api_url1": "http://api-osrm-bike.ops-tech:8080/route/v1/driving/",
        "max_distance": 30000,
        "group_id": "EXPRESS",
        "animated_url": "https://i.imgur.com/xiDxEYN.png",
        "requests": [
            {
                "_id": "SGN-EXPRESS-POD",
                "service_id": "SGN-EXPRESS",
                "enable": True,
                "name": "Thu hộ qua ví điện tử",
                "name_vi_vn": "Thu hộ qua ví điện tử",
                "name_en_us": "Collect payment via e-wallet",
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/icon-POD-extraservice.png",
                "img_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/IMG-POD-extraservice.png",
                "order": 0,
                "price": 0,
                "description_vi_vn": "Tài xế không cần ứng trước tiền thu hộ. Người nhận chỉ cần quét mã QR để thanh toán qua ví điện tử hoặc ứng dụng Mobile Banking khi tài xế đến giao hàng. Tiền thu hộ sẽ tự động chuyển vào tài khoản COD của bạn sau khi đơn hàng hoàn tất.",
                "description_en_us": "Your driver doesn't have to pay in advance. Upon delivery, the recipient scans a QR code to pay via an e-wallet or Mobile Banking app. Payment will be transferred to your COD account once the order is complete.",
                "type": "BOOLEAN",
                "description": "Người nhận thanh toán qua ví điện tử",
                "no_commission": True,
                "subtype": "POD",
                "applied_stp_num": 1,
                "max_pod": 290000,
                "capital_coefficient": 1,
                "service_group_id": "EXPRESS",
                "group_id": "POD"
            },
            {
                "_id": "SGN-INSTANT-FOOD-TRIP",
                "name": "Quay lại điểm lấy hàng",
                "enable": True,
                "name_vi_vn": "Quay lại điểm lấy hàng",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_round_trip.png",
                "name_en_us": "Return to the pick-up",
                "img_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_round_trip.png",
                "order": 1,
                "price": 0.8,
                "description_vi_vn": "- Tài xế sẽ quay lại điểm lấy hàng với số phí bằng 80% phí khoảng cách.\n\n- Lưu ý: Phí khoảng cách là số phí dựa theo số km vận chuyển, ko bao gồm phí điểm dừng và các loại phí khác.",
                "description_en_us": "- Tài xế sẽ quay lại điểm lấy hàng với số phí bằng 80% phí khoảng cách.\n\n- Lưu ý: Phí khoảng cách là số phí dựa theo số km vận chuyển, ko bao gồm phí điểm dừng và các loại phí khác.",
                "type": "COMMISSION_DISTANCE_PERCENTAGE",
                "description": "",
                "service_id": "SGN-EXPRESS",
                "service_group_id": "EXPRESS"
            },
            {
                "_id": "SGN-EXPRESS-THERMALBAG",
                "name": "Túi giữ nhiệt",
                "enable": True,
                "name_vi_vn": "Túi giữ nhiệt (Đang hoàn thiện)",
                "name_en_us": "Thermal Bag (Updating)",
                "icon_url": "https://trello-attachments.s3.amazonaws.com/5eabe9291dc6933e9e74eb2f/5f8531508904fa20c3cc89ad/1545287f04ffcc958416ab13b8bc3de5/2710.png",
                "order": 1,
                "price": 0,
                "description_vi_vn": "Đơn hàng sẽ được đảm bảo vận chuyển bằng túi giữ nhiệt của AhaMove, giúp khách hàng yên tâm về việc đảm bảo chất lượng hàng hóa 100% khi giao đến khách hàng. Phù hợp với sản phẩm là hàng tươi sống, đông lạnh, các mặt hàng đồ ăn thức uống cần đảm bảo nhiệt độ.",
                "description_en_us": "To make sure the quality of goods when delivered, each orders will be packed by AhaMove's thermal bags. Suitable for fresh, frozen food or beverages that need to be stored in Temperature-Controlled enviroment.",
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-EXPRESS",
                "supplier_description_url": "https://ahamove.com/tui-giu-nhiet-chuyen-nghiep-tung-giay/",
                "no_commission": False,
                "device_types": [
                    "web",
                    "android",
                    "ios"
                ],
                "available_districts": [
                    "VN.HC.QA",
                    "VN.HC.QB",
                    "VN.HC.QC",
                    "VN.HC.QD",
                    "VN.HC.QE",
                    "VN.HC.QF",
                    "VN.HC.QG",
                    "VN.HC.QH",
                    "VN.HC.QI",
                    "VN.HC.QJ",
                    "VN.HC.QK",
                    "VN.HC.QL",
                    "VN.HC.BT",
                    "VN.HC.BH",
                    "VN.HC.GV",
                    "VN.HC.PN",
                    "VN.HC.TB",
                    "VN.HC.TP",
                    "VN.HC.TD",
                    "VN.HC.BC",
                    "VN.HC.CG",
                    "VN.HC.CC",
                    "VN.HC.HM",
                    "VN.HC.NB"
                ],
                "service_group_id": "EXPRESS",
                "group_id": "THERMALBAG"
            },
            {
                "_id": "SGN-EXPRESS-FRAGILE",
                "name": "Giao hàng dễ vỡ",
                "enable": True,
                "name_vi_vn": "Giao hàng dễ vỡ",
                "name_en_us": "Fragile items delivery",
                "icon_url": "https://ahamove.com/wp-content/uploads/2021/07/ic_fragile_256x256.png",
                "img_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/fragile-2x.png",
                "order": 1,
                "price": 10000,
                "description_vi_vn": "Dịch vụ này bảo vệ tối đa hàng hóa của bạn khi vận chuyển. Bạn muốn chúng tôi nâng niu mặt hàng nào dưới đây?",
                "description_en_us": "This service protects your items to the highest level during delivery. What items would you like us to take care of?",
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-EXPRESS",
                "options": [
                    {
                        "code": "ITEM_1",
                        "name_vi_vn": "Bánh kem và các mặt hàng tương tự",
                        "name_en_us": "Cakes and similar items",
                        "selectable": True
                    },
                    {
                        "code": "ITEM_2",
                        "name_vi_vn": "Hoa và cây cảnh các loại",
                        "name_en_us": "Flowers and plants",
                        "selectable": True
                    },
                    {
                        "code": "ITEM_3",
                        "name_vi_vn": "Sản phẩm đựng trong chai/lọ/bình dễ vỡ",
                        "name_en_us": "Bottles and other breakable items",
                        "selectable": True
                    },
                    {
                        "code": "ITEM_4",
                        "name_vi_vn": "Sản phẩm làm bằng thủy tinh/gốm sứ/đất nung",
                        "name_en_us": "Glass, porcelain, pottery and other ceramics",
                        "selectable": True
                    },
                    {
                        "code": "ITEM_5",
                        "name_vi_vn": "Hàng hóa, thiết bị điện tử",
                        "name_en_us": "Electronic devices",
                        "selectable": True
                    },
                    {
                        "code": "ITEM_6",
                        "name_vi_vn": "Khác (vui lòng nêu rõ)",
                        "name_en_us": "Other (please specify)",
                        "selectable": True,
                        "need_user_input": True
                    }
                ],
                "max_distance": 10000,
                "service_group_id": "EXPRESS",
                "group_id": "FRAGILE"
            },
            {
                "_id": "SGN-EXPRESS-INSURANCE",
                "name": "Khai giá hàng hoá",
                "name_vi_vn": "Khai giá hàng hoá",
                "name_en_us": "Value declaration",
                "enable": True,
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/Insurance/secure+24x24%402x.png",
                "order": 1.0,
                "price_blocks": [
                    {
                        "from": 0,
                        "to": 5000001,
                        "price": 1000,
                        "description_vi_vn": "Bồi thường mất mát hoặc hư hỏng theo giá trị hàng hoá của bạn",
                        "description_en_us": "Coverage for loss or damage according to the value of your items"
                    },
                    {
                        "from": 5000001,
                        "to": 10000001,
                        "price": 2000,
                        "description_vi_vn": "Bồi thường mất mát hoặc hư hỏng theo giá trị hàng hoá của bạn",
                        "description_en_us": "Coverage for loss or damage according to the value of your items"
                    },
                    {
                        "from": 10000001,
                        "to": 30000000,
                        "price": 10000,
                        "description_vi_vn": "Bồi thường mất mát hoặc hư hỏng theo giá trị hàng hoá của bạn",
                        "description_en_us": "Coverage for loss or damage according to the value of your items"
                    }
                ],
                "no_supplier_payout": True,
                "type": "COD_INSURANCE",
                "applied_stp_num": 12.0,
                "service_id": "SGN-EXPRESS",
                "description_url": "https://www.ahamove.com/tinh-nang-dam-bao-hang-hoa-100/",
                "benefit_url": "https://ahamove.com/dam-bao-don-hang-danh-cho-khach-hang/",
                "none_cod_price_blocks": {
                    "electronics": 1000,
                    "health & beauty": 1000,
                    "housing & lifestyle": 1000,
                    "food": 1000,
                    "mother & baby": 1000,
                    "fashion": 1000,
                    "grocery": 1000,
                    "restaurant": 1000,
                    "sport": 1000,
                    "drink": 1000,
                    "other": 1000,
                    "individual needs": 1000,
                    "transportation": 1000
                },
                "non_cod_description": "Bồi thường mất mát hoặc hư hỏng theo danh mục hàng hoá của bạn",
                "service_group_id": "EXPRESS",
                "group_id": "INSURANCE"
            },
            {
                "_id": "SGN-EXPRESS-TRANSFER-COD",
                "name": "Nộp tiền thu hộ",
                "enable": True,
                "name_vi_vn": "Nộp tiền thu hộ",
                "name_en_us": "Collect COD",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_d2d.png",
                "order": 1,
                "price": 0,
                "no_commission": True,
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-EXPRESS",
                "transfer_cod": True,
                "service_group_id": "EXPRESS",
                "group_id": "COD"
            },
            {
                "_id": "SGN-EXPRESS-H2H",
                "name": "Hand-to-hand",
                "enable": True,
                "name_vi_vn": "Hỗ trợ giao hàng tận tay",
                "name_en_us": "Hand to hand delivery",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_d2d.png",
                "img_url": "http://file.hstatic.net/1000010797/file/hand-to-hand.png",
                "order": 3,
                "price": 10000,
                "max_input": 6,
                "no_commission": True,
                "description_vi_vn": "Khách hàng hỗ trợ chi phí giao hàng tận tay cho tài xế trong trường hợp các điểm giao thuộc chung cư,  cơ quan, bệnh viện,...Hãy chọn số lượng tương ứng với số điểm giao hàng bạn cần tài xế giao tận tay.",
                "description_en_us": "Customer can request driver for hand to hand delivery service if drop off point is an apartment, an office , a hospital or a building. Please select the number of drop off points that need hand to hand delivery.",
                "type": "PER_UNIT",
                "description": "",
                "service_id": "SGN-EXPRESS",
                "service_group_id": "EXPRESS",
                "group_id": "H2H"
            },
            {
                "_id": "SGN-EXPRESS-D2D",
                "name": "Giao hàng tận tay",
                "enable": True,
                "name_vi_vn": "Giao hàng tận tay",
                "name_en_us": "Giao hàng tận tay",
                "icon_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/core_services/req_d2d.png",
                "order": 3,
                "price": 10000,
                "no_commission": True,
                "type": "BOOLEAN",
                "service_id": "SGN-EXPRESS",
                "delivery_option": True,
                "img_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/core_services/req_d2d.png",
                "description_vi_vn": "Khách hàng có thể chọn được từng điểm giao để yêu cầu tài xế giao hàng tới tận tay người nhận.",
                "description_en_us": "Khách hàng có thể chọn được từng điểm giao để yêu cầu tài xế giao hàng tới tận tay người nhận.",
                "description_url": "https://ahamove.com/gioi-thieu-tinh-nang-giao-hang-tan-tay/",
                "service_group_id": "EXPRESS",
                "group_id": "D2D"
            },
            {
                "_id": "SGN-EXPRESS-TIP",
                "name": "Hỗ trợ tài xế",
                "enable": True,
                "name_vi_vn": "Hỗ trợ tài xế",
                "name_en_us": "Tipping",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/sr_tipping.png",
                "img_url": "http://file.hstatic.net/1000010797/file/tipping_final.jpg",
                "order": 4,
                "price": 5000,
                "max_input": 5,
                "no_commission": True,
                "description_vi_vn": "Hãy chọn dịch vụ này nếu bạn muốn hỗ trợ tài xế trong giờ cao điểm, khi thời tiết khó khăn, hoặc đơn giản là muốn thưởng thêm cho tài xế. Ngoài ra, tính năng này sẽ giúp cho đơn hàng của bạn được ưu tiên hơn trong thời gian cao điểm.",
                "description_en_us": "This will show your support or compliment to the driver, especially in rush hours, hand to hand delivery, bad weather. Also, this feature will prioritize your request in peak time.",
                "type": "PER_UNIT",
                "description": "",
                "service_id": "SGN-EXPRESS",
                "service_group_id": "EXPRESS",
                "group_id": "TIP"
            }
        ],
        "currency": "VND"
    },
    {
        "_id": "SGN-POOL",
        "commission_type": "PERCENTAGE",
        "require_to": True,
        "require_request": False,
        "rebroadcast_interval": 1200,
        "parent_id": "",
        "city_id": "SGN",
        "enable": True,
        "name": "Siêu Rẻ",
        "name_vi_vn": "Siêu Rẻ",
        "name_en_us": "Siêu Rẻ",
        "require_pod": False,
        "icon_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/aha-service/SieuRe.jpg",
        "map_icon_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/core_services/xe1-02.png",
        "order": 3,
        "broadcast_distance": 2500,
        "advance_broadcast_distance": 2500,
        "stop_fee": 5000,
        "timeout": 1800,
        "cod": 1000000,
        "first_order_cod": 1,
        "description": "Save 20%, 2-hour delivery",
        "description_vi_vn": "Giao hàng tối đa 2 giờ, tiết kiệm 20%",
        "distance_fee": "(20000 if x <= 4 else 20000 + (x - 4) * 4400)",
        "commission_value": 0.212,
        "max_concurrent_orders": 4,
        "max_stop_points": 2,
        "is_insured": False,
        "fee_description_vi_vn": "Thời gian: tối đa 2 giờ (áp dụng \nđơn hàng dưới 6km)\n\nSố điểm giao tối đa: 1\n\nPhí quãng đường:\n- 4km đầu: 20,000đ\n- Trên 4km: 4,400đ/km\n\nTrọng lượng tiêu chuẩn: 30kg\nKích thước tiêu chuẩn: 50x40x50\n\nMức COD tối đa: 1,000,000đ\nPhí COD: Miễn phí",
        "fee_description_en_us": "Leadtime: Maximum :2H\n(distance under 6km)\n\nMaximum drop off: 1\n\n\n\nDistance fee:\n- First 4 km: 20,000 VND\n- Over 4 km: 4,400 VND/km\n\nPayload capacity: 30kg\nSuitable goods (LxWxH): 50x40x50 cm\n\n\nMaximum COD: 1,000,000 VND \nCOD fee: Free",
        "description_en_us": "Giao hàng tối đa 2 giờ, tiết kiệm 20%",
        "supplier_description": "Dịch vụ Siêu rẻ được thực hiện trong vòng 1 tiếng 45 phút, được nhận tối đa 3 đơn hàng",
        "notify_package_return": True,
        "pending_period": 180,
        "cross_service": {
            "enable": True,
            "services": [
                "SGN-POOL",
                "SGN-SAMEDAY-INTERNAL",
                "SGN-TMDT",
                "SGN-2H-INTERNAL"
            ]
        },
        "event_callback": False,
        "rebroadcast_limit": 1,
        "uniform_verify": False,
        "uniform_verify_message_en_us": "Is your driver wearing proper uniform (including AhaMove's jacket, helmet)?",
        "uniform_verify_message_vi_vn": "Tài xế có mang đồng phục (áo, nón) hay không?",
        "set_idle_status_when_creating_order": False,
        "max_cod": 1000000,
        "max_cod_per_stop_point": 1000000,
        "delay_time": 3,
        "delivery_type": "INSTANT",
        "distance_fee_v3": {
            "blocks": [
                {
                    "from": 0,
                    "to": 4,
                    "base": 20000,
                    "price_multiplier": 0
                },
                {
                    "from": 4,
                    "to": 100000,
                    "base": 20000,
                    "price_multiplier": 4400
                }
            ],
            "hour_rates": []
        },
        "available_districts": [
            "VN.HC.BC",
            "VN.HC.CC",
            "VN.HC.CG",
            "VN.HC.HM",
            "VN.HC.NB",
            "VN.HC.BH",
            "VN.HC.BT",
            "VN.HC.GV",
            "VN.HC.PN",
            "VN.HC.QJ",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.QA",
            "VN.HC.QB",
            "VN.HC.QC",
            "VN.HC.QD",
            "VN.HC.QE",
            "VN.HC.QF",
            "VN.HC.QG",
            "VN.HC.QH",
            "VN.HC.QI",
            "VN.HC.TB",
            "VN.HC.TP",
            "VN.HC.TD"
        ],
        "payment_method": [
            {
                "description": "Cash",
                "description_vi_vn": "Tiền mặt",
                "payment": "cash",
                "order": 1
            },
            {
                "description": "Balance",
                "description_vi_vn": "Ví AhaMove",
                "payment": "balance",
                "order": 2
            },
            {
                "description": "MoMo e-Wallet",
                "description_vi_vn": "Ví điện tử MoMo",
                "payment": "momo",
                "order": 3
            },
            {
                "description": "ZaloPay e-Wallet",
                "description_vi_vn": "Ví điện tử ZaloPay",
                "payment": "Zalopay",
                "order": 4
            }
        ],
        "enable_platform": [
            "momo_deeplink",
            "momo_permission",
            "zalo",
            "zalopay",
            "smartpay_deeplink",
            "viettel-pay_deeplink",
            "shopee-pay_deeplink"
        ],
        "same_district_delivery": False,
        "same_district_delivery_areas": [
            "VN.HCM.ZONE"
        ],
        "applied_pandemic_hours_areas": [
            "VN.BH",
            "VN.PC.BT",
            "VN.PC.NK",
            "VN.PC.CR",
            "VN.PC.VT",
            "VN.PC.PD",
            "VN.PC.TN",
            "VN.PC.TL",
            "VN.PC.CD",
            "VN.PC.OM"
        ],
        "cross_city": {
            "enable": True,
            "cities": [
                "SGN"
            ]
        },
        "assigning_list_order": 3,
        "supplier_description_vi_vn": "Dịch vụ Siêu rẻ được thực hiện trong vòng 1 tiếng 45 phút, được nhận tối đa 3 đơn hàng",
        "group_name_en_us": "Tiết kiệm",
        "group_name_vi_vn": "Tiết kiệm",
        "recommendation_config": {
            "supplier_timeout": 20,
            "recommend_timeout": 60,
            "recommend_radius": 700,
            "sleep_interval": 60,
            "dispatch_mode": "RECOMMEND",
            "pool_mode": "NO_POOL",
            "pool_saving_threshold": 0.2,
            "poolable": False
        },
        "supplier_description_url": "https://ahamove.com/quy-trinh-giao-hang-dich-vu-co-ban",
        "advance_max_concurrent_orders": 4,
        "vat_rate": 0.1,
        "priority_score": 6,
        "route_api_url": "http://route.ahamove.com/v5.22.0/route/v1/driving/",
        "is_tip_allowed": True,
        "truck_ban": {
            "ban_hours": []
        },
        "group_id": "POOL",
        "animated_url": "https://i.imgur.com/xiDxEYN.png",
        "requests": [
            {
                "_id": "SGN-POOL-POD",
                "service_id": "SGN-POOL",
                "enable": True,
                "name": "Thu hộ qua ví điện tử",
                "name_vi_vn": "Thu hộ qua ví điện tử",
                "name_en_us": "Collect payment via e-wallet",
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/icon-POD-extraservice.png",
                "img_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/IMG-POD-extraservice.png",
                "order": 0,
                "price": 0,
                "description_vi_vn": "Tài xế không cần ứng trước tiền thu hộ. Người nhận chỉ cần quét mã QR để thanh toán qua ví điện tử hoặc ứng dụng Mobile Banking khi tài xế đến giao hàng. Tiền thu hộ sẽ tự động chuyển vào tài khoản COD của bạn sau khi đơn hàng hoàn tất.",
                "description_en_us": "Your driver doesn't have to pay in advance. Upon delivery, the recipient scans a QR code to pay via an e-wallet or Mobile Banking app. Payment will be transferred to your COD account once the order is complete.",
                "type": "BOOLEAN",
                "description": "Người nhận thanh toán qua ví điện tử",
                "no_commission": True,
                "subtype": "POD",
                "applied_stp_num": 1,
                "max_pod": 2000000,
                "capital_coefficient": 1.5,
                "service_group_id": "POOL",
                "group_id": "POD"
            },
            {
                "_id": "SGN-POOL-TRANSFER-COD",
                "name": "Nộp tiền thu hộ",
                "enable": True,
                "support_remarks": True,
                "name_vi_vn": "Nộp tiền thu hộ",
                "name_en_us": "Nộp tiền thu hộ",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_d2d.png",
                "order": 1,
                "price": 0,
                "no_commission": True,
                "type": "BOOLEAN",
                "service_id": "SGN-POOL",
                "transfer_cod": True,
                "img_url": "http://file.hstatic.net/1000010797/file/hand-to-hand.png",
                "service_group_id": "POOL",
                "group_id": "COD"
            },
            {
                "_id": "SGN-POOL-INSURANCE",
                "name": "Khai giá hàng hoá",
                "name_vi_vn": "Khai giá hàng hoá",
                "name_en_us": "Value declaration",
                "enable": True,
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/Insurance/secure+24x24%402x.png",
                "order": 1.0,
                "price_blocks": [
                    {
                        "from": 0,
                        "to": 5000001,
                        "price": 1000,
                        "description_vi_vn": "Bồi thường mất mát hoặc hư hỏng theo giá trị hàng hoá của bạn",
                        "description_en_us": "Coverage for loss or damage according to the value of your items"
                    },
                    {
                        "from": 5000001,
                        "to": 10000001,
                        "price": 2000,
                        "description_vi_vn": "Bồi thường mất mát hoặc hư hỏng theo giá trị hàng hoá của bạn",
                        "description_en_us": "Coverage for loss or damage according to the value of your items"
                    },
                    {
                        "from": 10000001,
                        "to": 30000000,
                        "price": 10000,
                        "description_vi_vn": "Bồi thường mất mát hoặc hư hỏng theo giá trị hàng hoá của bạn",
                        "description_en_us": "Coverage for loss or damage according to the value of your items"
                    }
                ],
                "no_supplier_payout": True,
                "type": "COD_INSURANCE",
                "applied_stp_num": 12.0,
                "service_id": "SGN-POOL",
                "description_url": "https://www.ahamove.com/tinh-nang-dam-bao-hang-hoa-100/",
                "benefit_url": "https://ahamove.com/dam-bao-don-hang-danh-cho-khach-hang/",
                "none_cod_price_blocks": {
                    "electronics": 1000,
                    "health & beauty": 1000,
                    "housing & lifestyle": 1000,
                    "food": 1000,
                    "mother & baby": 1000,
                    "fashion": 1000,
                    "grocery": 1000,
                    "restaurant": 1000,
                    "sport": 1000,
                    "drink": 1000,
                    "other": 1000,
                    "individual needs": 1000,
                    "transportation": 1000
                },
                "non_cod_description": "Bồi thường mất mát hoặc hư hỏng theo danh mục hàng hoá của bạn",
                "service_group_id": "POOL",
                "group_id": "INSURANCE"
            },
            {
                "_id": "SGN-POOL-ROUND-TRIP",
                "name": "Quay lại điểm lấy hàng",
                "enable": True,
                "name_vi_vn": "Quay lại điểm lấy hàng",
                "name_en_us": "Return to pick up location",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_round_trip.png",
                "img_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_round_trip.png",
                "order": 2,
                "description_vi_vn": "Tài xế sẽ quay lại điểm lấy hàng với số phí bằng 80% phí khoảng cách. Lưu ý: Phí khoảng cách là số phí dựa theo số km vận chuyển, ko bao gồm phí điểm dừng và các loại phí khác.",
                "description_en_us": "Driver will return to pick up location for 80% of distance fee. Note: Distance fee is calculated solely by the travel distance, it does not include stop fee and others fee",
                "type": "COMMISSION_DISTANCE_PERCENTAGE",
                "price": 0.8,
                "description": "",
                "service_id": "SGN-POOL",
                "supplier_description": "Tài xế sẽ quay lại điểm lấy hàng với số phí bằng 80% phí khoảng cách. Lưu ý: Phí khoảng cách là số phí dựa theo số km vận chuyển, ko bao gồm phí điểm dừng và các loại phí khác.",
                "service_group_id": "POOL"
            },
            {
                "_id": "tao_story_138",
                "name": "Táo Story 138 (1kg)",
                "name_vi_vn": "Táo Story 138 (1kg)",
                "name_en_us": "Táo Story 138 (1kg)",
                "icon_url": "https://images.foody.vn/res/g8/77545/s120x120/3471ba73-d07a-4463-ab6b-23d755fb52a5.jpg",
                "order": 2,
                "price": 61750,
                "max_input": 2,
                "type": "PER_UNIT",
                "description": "",
                "service_id": "SGN-POOL",
                "enable": True,
                "no_commission": True,
                "service_group_id": "POOL"
            },
            {
                "_id": "tao_story_139",
                "name": "Mận Story 139 (1kg)",
                "name_vi_vn": "Táo Story 139 (1kg)",
                "name_en_us": "Táo Story 139 (1kg)",
                "icon_url": "https://images.foody.vn/res/g8/77545/s120x120/3471ba73-d07a-4463-ab6b-23d755fb52a5.jpg",
                "order": 2,
                "price": 61750,
                "max_input": 2,
                "type": "PER_UNIT",
                "description": "",
                "service_id": "SGN-POOL",
                "enable": True,
                "no_commission": True,
                "service_group_id": "POOL"
            },
            {
                "_id": "tao_story_140",
                "name": "Ổi Story 140 (1kg)",
                "name_vi_vn": "Ổi  Story 140 (1kg)",
                "name_en_us": "Ổi  Story 140 (1kg)",
                "icon_url": "https://images.foody.vn/res/g8/77545/s120x120/3471ba73-d07a-4463-ab6b-23d755fb52a5.jpg",
                "order": 2,
                "price": 61750,
                "max_input": 2,
                "type": "PER_UNIT",
                "description": "",
                "service_id": "SGN-POOL",
                "enable": True,
                "no_commission": True,
                "service_group_id": "POOL"
            },
            {
                "_id": "tao_story_141",
                "name": "Táo Story 140 (1kg)",
                "name_vi_vn": "Táo Story 140 (1kg)",
                "name_en_us": "Táo Story 140 (1kg)",
                "icon_url": "https://images.foody.vn/res/g8/77545/s120x120/3471ba73-d07a-4463-ab6b-23d755fb52a5.jpg",
                "order": 2,
                "price": 61750,
                "max_input": 2,
                "type": "PER_UNIT",
                "description": "",
                "service_id": "SGN-POOL",
                "enable": True,
                "no_commission": True,
                "service_group_id": "POOL"
            },
            {
                "_id": "tao_story_142",
                "name": "Táo Story 140 (1kg)",
                "name_vi_vn": "Táo Story 140 (1kg)",
                "name_en_us": "Táo Story 140 (1kg)",
                "icon_url": "https://images.foody.vn/res/g8/77545/s120x120/3471ba73-d07a-4463-ab6b-23d755fb52a5.jpg",
                "order": 2,
                "price": 61750,
                "max_input": 2,
                "type": "PER_UNIT",
                "description": "",
                "service_id": "SGN-POOL",
                "enable": True,
                "no_commission": True,
                "service_group_id": "POOL"
            },
            {
                "_id": "tao_story_143",
                "name": "Táo Story 140 (1kg)",
                "name_vi_vn": "Táo Story 140 (1kg)",
                "name_en_us": "Táo Story 140 (1kg)",
                "icon_url": "https://images.foody.vn/res/g8/77545/s120x120/3471ba73-d07a-4463-ab6b-23d755fb52a5.jpg",
                "order": 2,
                "price": 61750,
                "max_input": 2,
                "type": "PER_UNIT",
                "description": "",
                "service_id": "SGN-POOL",
                "enable": True,
                "no_commission": True,
                "service_group_id": "POOL"
            },
            {
                "_id": "tao_story_144",
                "name": "Táo Story 140 (1kg)",
                "name_vi_vn": "Táo Story 140 (1kg)",
                "name_en_us": "Táo Story 140 (1kg)",
                "icon_url": "https://images.foody.vn/res/g8/77545/s120x120/3471ba73-d07a-4463-ab6b-23d755fb52a5.jpg",
                "order": 2,
                "price": 61750,
                "max_input": 2,
                "type": "PER_UNIT",
                "description": "",
                "service_id": "SGN-POOL",
                "enable": True,
                "no_commission": True,
                "service_group_id": "POOL"
            },
            {
                "_id": "tao_story_145",
                "name": "Táo Story 140 (1kg)",
                "name_vi_vn": "Táo Story 140 (1kg)",
                "name_en_us": "Táo Story 140 (1kg)",
                "icon_url": "https://images.foody.vn/res/g8/77545/s120x120/3471ba73-d07a-4463-ab6b-23d755fb52a5.jpg",
                "order": 2,
                "price": 61750,
                "max_input": 2,
                "type": "PER_UNIT",
                "description": "",
                "service_id": "SGN-POOL",
                "enable": True,
                "no_commission": True,
                "service_group_id": "POOL"
            },
            {
                "_id": "tao_story_146",
                "name": "Táo Story 140 (1kg)",
                "name_vi_vn": "Táo Story 140 (1kg)",
                "name_en_us": "Táo Story 140 (1kg)",
                "icon_url": "https://images.foody.vn/res/g8/77545/s120x120/3471ba73-d07a-4463-ab6b-23d755fb52a5.jpg",
                "order": 2,
                "price": 61750,
                "max_input": 2,
                "type": "PER_UNIT",
                "description": "",
                "service_id": "SGN-POOL",
                "enable": True,
                "no_commission": True,
                "service_group_id": "POOL"
            },
            {
                "_id": "tao_story_147",
                "name": "Táo Story 140 (1kg)",
                "name_vi_vn": "Táo Story 140 (1kg)",
                "name_en_us": "Táo Story 140 (1kg)",
                "icon_url": "https://images.foody.vn/res/g8/77545/s120x120/3471ba73-d07a-4463-ab6b-23d755fb52a5.jpg",
                "order": 2,
                "price": 61750,
                "max_input": 2,
                "type": "PER_UNIT",
                "description": "",
                "service_id": "SGN-POOL",
                "enable": True,
                "no_commission": True,
                "service_group_id": "POOL"
            },
            {
                "_id": "tao_story_148",
                "name": "Táo Story 140 (1kg)",
                "name_vi_vn": "Táo Story 140 (1kg)",
                "name_en_us": "Táo Story 140 (1kg)",
                "icon_url": "https://images.foody.vn/res/g8/77545/s120x120/3471ba73-d07a-4463-ab6b-23d755fb52a5.jpg",
                "order": 2,
                "price": 61750,
                "max_input": 2,
                "type": "PER_UNIT",
                "description": "",
                "service_id": "SGN-POOL",
                "enable": True,
                "no_commission": True,
                "service_group_id": "POOL"
            },
            {
                "_id": "tao_story_149",
                "name": "Táo Story 140 (1kg)",
                "name_vi_vn": "Táo Story 140 (1kg)",
                "name_en_us": "Táo Story 140 (1kg)",
                "icon_url": "https://images.foody.vn/res/g8/77545/s120x120/3471ba73-d07a-4463-ab6b-23d755fb52a5.jpg",
                "order": 2,
                "price": 61750,
                "max_input": 2,
                "type": "PER_UNIT",
                "description": "",
                "service_id": "SGN-POOL",
                "enable": True,
                "no_commission": True,
                "service_group_id": "POOL"
            },
            {
                "_id": "tao_story_150",
                "name": "Táo Story 140 (1kg)",
                "name_vi_vn": "Táo Story 140 (1kg)",
                "name_en_us": "Táo Story 140 (1kg)",
                "icon_url": "https://images.foody.vn/res/g8/77545/s120x120/3471ba73-d07a-4463-ab6b-23d755fb52a5.jpg",
                "order": 2,
                "price": 61750,
                "max_input": 2,
                "type": "PER_UNIT",
                "description": "",
                "service_id": "SGN-POOL",
                "enable": True,
                "no_commission": True,
                "service_group_id": "POOL"
            },
            {
                "_id": "kiwi_vang",
                "name": "Kiwi vàng (1kg)",
                "name_vi_vn": "Kiwi vàng (1kg)",
                "name_en_us": "Kiwi vàng (1kg)",
                "icon_url": "http://luontuoisach.vn/public/files/upload/product/1491014712kiwi-vang-fristgold.jpg",
                "order": 3,
                "price": 208050,
                "max_input": 2,
                "type": "PER_UNIT",
                "description": "",
                "service_id": "SGN-POOL",
                "enable": True,
                "no_commission": True,
                "service_group_id": "POOL"
            },
            {
                "_id": "SGN-POOL-TIP",
                "name": "Hỗ trợ tài xế",
                "enable": True,
                "name_vi_vn": "Hỗ trợ tài xế",
                "name_en_us": "Tipping",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/sr_tipping.png",
                "img_url": "http://file.hstatic.net/1000010797/file/tipping_final.jpg",
                "order": 4,
                "no_commission": True,
                "description_vi_vn": "Hãy chọn dịch vụ này nếu bạn muốn hỗ trợ tài xế trong giờ cao điểm, khi cần giao hàng lên lầu, nơi phải tốn phí giữ xe, khi thời tiết khó khăn, hoặc đơn giản là muốn thưởng thêm cho tài xế. Ngoài ra, tính năng này sẽ giúp cho đơn hàng của bạn được ưu tiên hơn trong thời gian cao điểm.",
                "description_en_us": "This will show your support or compliment to the driver, especially in rush hours, hand to hand delivery, bad weather. Also, this feature will prioritize your request in peak time.",
                "type": "PER_UNIT",
                "price": 5000,
                "description": "",
                "service_id": "SGN-POOL",
                "max_input": 6,
                "no_promotion": True,
                "service_group_id": "POOL",
                "group_id": "TIP"
            },
            {
                "_id": "Tao_regal_queen_1",
                "name": "Táo Regal Queen size 100- 110-120 (1kg)",
                "name_vi_vn": "Táo Regal Queen size 100- 110-120 (1kg)",
                "name_en_us": "Táo Regal Queen size 100- 110-120 (1kg)",
                "icon_url": "http://luontuoisach.vn/public/files/upload/product/1586842999queen02.jpg",
                "order": 4,
                "price": 65550,
                "max_input": 2,
                "type": "PER_UNIT",
                "description": "",
                "service_id": "SGN-POOL",
                "enable": True,
                "no_commission": True,
                "service_group_id": "POOL"
            }
        ],
        "currency": "VND"
    },
    {
        "_id": "SGN-SAMEDAY",
        "set_idle_status_when_creating_order": True,
        "idle_timeout": 1200,
        "timeout": 1200,
        "commission_type": "PERCENTAGE",
        "require_to": True,
        "require_request": False,
        "rebroadcast_interval": 4800,
        "rebroadcast_limit": 12,
        "max_distance": 25000,
        "city_id": "SGN",
        "enable": True,
        "name": "4H",
        "name_vi_vn": "4H",
        "name_en_us": "4H",
        "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/sp-sameday.png",
        "map_icon_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/core_services/xe1-02.png",
        "order": 4,
        "broadcast_distance": 2000,
        "advance_broadcast_distance": 5000,
        "stop_fee": 0,
        "cod": 1000000,
        "max_cod": 1000000,
        "first_order_cod": 1,
        "description": "Giao hàng nội thành, cam kết trong 4 giờ*",
        "description_vi_vn": "Giao hàng nội thành, cam kết trong 4 giờ*",
        "distance_fee": "0",
        "partner_distance_fee": "(27000 if x <= 10 else 36000 if x <= 15 else 42000 if x <= 20 else 42000 + (x-20)*5500)",
        "vat_rate": 0.1,
        "commission_value": 0.212,
        "max_concurrent_orders": 4,
        "max_stop_points": 3,
        "fee_description_vi_vn": "Bảng giá:\n0 - 10km: đ22.000\n10 - 15km: đ27.000\n15 - 20km: đ32.000\nGiờ đặt đơn: 9h - 17h\nCOD tối đa: đ500.000. Trọng lượng tối đa: 5kg. Kích thước tối đa: 25(D)x32(R)x12(C)cm\n* Giao hàng 4 giờ áp dụng cho đơn hàng dưới 15km.",
        "fee_description_en_us": "Bảng giá:\n0 - 10km: đ22.000\n10 - 15km: đ27.000\n15 - 20km: đ32.000\nGiờ đặt đơn: 9h - 17h\nCOD tối đa: đ500.000. Trọng lượng tối đa: 5kg. Kích thước tối đa: 25(D)x32(R)x12(C)cm\n* Giao hàng 4 giờ áp dụng cho đơn hàng dưới 15km.",
        "description_en_us": "Giao hàng nội thành, cam kết trong 4 giờ*",
        "planner_config": {
            "enable": True,
            "base_price": 22000,
            "epd_target": 5,
            "vehicle_capacity": 6,
            "idle_timeout": 300,
            "outlier_service_id": "SGN-POOL",
            "dispatch_mode": "AUTO_ASSIGN",
            "matching_rate": 0.5,
            "matching_timeout": 0,
            "outlier_max_distance": 25000,
            "max_distance": 25000,
            "current_stop_loss": 15000,
            "end_day_epd": 4.5,
            "stop_loss": 1200000,
            "current_outlier_loss": -336000
        },
        "cross_service": {
            "enable": True,
            "services": [
                "SGN-DG",
                "SGN-POOL"
            ]
        },
        "cross_city": {
            "enable": True,
            "cities": [
                "SGN"
            ]
        },
        "available_districts": [
            "VN.HC.BC",
            "VN.HC.BH",
            "VN.HC.BT",
            "VN.HC.GV",
            "VN.HC.PN",
            "VN.HC.QJ",
            "VN.HC.QK",
            "VN.HC.QA",
            "VN.HC.QC",
            "VN.HC.QD",
            "VN.HC.QE",
            "VN.HC.QF",
            "VN.HC.QG",
            "VN.HC.QH",
            "VN.HC.TB",
            "VN.HC.TP",
            "VN.HC.TD"
        ],
        "delivery_type": "SAMEDAY",
        "notify_package_return": True,
        "uniform_verify": True,
        "max_cod_per_stop_point": 1000000,
        "service_hours": {
            "0": [
                {
                    "start_time": 540,
                    "end_time": 660
                },
                {
                    "start_time": 660,
                    "end_time": 780
                },
                {
                    "start_time": 780,
                    "end_time": 900
                },
                {
                    "start_time": 900,
                    "end_time": 1020
                }
            ],
            "1": [
                {
                    "start_time": 540,
                    "end_time": 660
                },
                {
                    "start_time": 660,
                    "end_time": 780
                },
                {
                    "start_time": 780,
                    "end_time": 900
                },
                {
                    "start_time": 900,
                    "end_time": 1020
                }
            ],
            "2": [
                {
                    "start_time": 540,
                    "end_time": 660
                },
                {
                    "start_time": 660,
                    "end_time": 780
                },
                {
                    "start_time": 780,
                    "end_time": 900
                },
                {
                    "start_time": 900,
                    "end_time": 1020
                }
            ],
            "3": [
                {
                    "start_time": 540,
                    "end_time": 660
                },
                {
                    "start_time": 660,
                    "end_time": 780
                },
                {
                    "start_time": 780,
                    "end_time": 900
                },
                {
                    "start_time": 900,
                    "end_time": 1020
                }
            ],
            "4": [
                {
                    "start_time": 540,
                    "end_time": 660
                },
                {
                    "start_time": 660,
                    "end_time": 780
                },
                {
                    "start_time": 780,
                    "end_time": 900
                },
                {
                    "start_time": 900,
                    "end_time": 1020
                }
            ],
            "5": [
                {
                    "start_time": 540,
                    "end_time": 660
                },
                {
                    "start_time": 660,
                    "end_time": 780
                },
                {
                    "start_time": 780,
                    "end_time": 900
                },
                {
                    "start_time": 900,
                    "end_time": 1020
                }
            ],
            "6": [
                {
                    "start_time": 540,
                    "end_time": 660
                },
                {
                    "start_time": 660,
                    "end_time": 780
                },
                {
                    "start_time": 780,
                    "end_time": 900
                },
                {
                    "start_time": 900,
                    "end_time": 1020
                }
            ]
        },
        "parent_id": "",
        "enable_platform": [
            "momo_deeplink",
            "momo_permission",
            "zalo",
            "zalopay",
            "smartpay_deeplink",
            "viettel-pay_deeplink"
        ],
        "group_name_en_us": "Budget delivery",
        "group_name_vi_vn": "Tiết kiệm",
        "recommendation_config": {
            "supplier_timeout": 20,
            "recommend_timeout": 100,
            "recommend_radius": 500,
            "sleep_interval": 300,
            "dispatch_mode": "RECOMMEND",
            "pool_mode": "NO_POOL",
            "pool_saving_threshold": 0.2,
            "poolable": False
        },
        "transfer_cod": True,
        "partner_distance_fee_v3": {
            "blocks": [
                {
                    "from": 0,
                    "to": 10,
                    "base": 27000,
                    "price_multiplier": 0
                },
                {
                    "from": 10,
                    "to": 15,
                    "base": 36000,
                    "price_multiplier": 0
                },
                {
                    "from": 15,
                    "to": 20,
                    "base": 42000,
                    "price_multiplier": 0
                },
                {
                    "from": 20,
                    "to": 1000,
                    "base": 42000,
                    "price_multiplier": 5500
                }
            ],
            "hour_rates": []
        },
        "opening_hours": "7-23",
        "priority_score": 6,
        "is_tip_allowed": True,
        "is_child_service": True,
        "distance_fee_v3": {
            "blocks": [
                {
                    "from": 0,
                    "to": 100000,
                    "base": 0,
                    "price_multiplier": 0
                }
            ],
            "hour_rates": []
        },
        "group_id": "4H",
        "animated_url": "https://i.imgur.com/xiDxEYN.png",
        "requests": [
            {
                "_id": "SGN-SAMEDAY-POD",
                "service_id": "SGN-SAMEDAY",
                "enable": True,
                "name": "Thu hộ qua ví điện tử",
                "name_vi_vn": "Thu hộ qua ví điện tử",
                "name_en_us": "Collect payment via e-wallet",
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/icon-POD-extraservice.png",
                "img_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/IMG-POD-extraservice.png",
                "order": 0,
                "price": 0,
                "description_vi_vn": "Tài xế không cần ứng trước tiền thu hộ. Người nhận chỉ cần quét mã QR để thanh toán qua ví điện tử hoặc ứng dụng Mobile Banking khi tài xế đến giao hàng. Tiền thu hộ sẽ tự động chuyển vào tài khoản COD của bạn sau khi đơn hàng hoàn tất.",
                "description_en_us": "Your driver doesn't have to pay in advance. Upon delivery, the recipient scans a QR code to pay via an e-wallet or Mobile Banking app. Payment will be transferred to your COD account once the order is complete.",
                "type": "BOOLEAN",
                "description": "Người nhận thanh toán qua ví điện tử",
                "no_commission": True,
                "subtype": "epayment_on_delivery",
                "applied_stp_num": 1,
                "max_pod": 2000000,
                "service_group_id": "4H"
            },
            {
                "_id": "SGN-SAMEDAY-TRANSFER-COD",
                "name": "Nộp tiền thu hộ",
                "enable": True,
                "support_remarks": True,
                "name_vi_vn": "Nộp tiền thu hộ",
                "name_en_us": "Nộp tiền thu hộ",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_d2d.png",
                "order": 1,
                "price": 0,
                "no_commission": True,
                "type": "BOOLEAN",
                "service_id": "SGN-SAMEDAY",
                "img_url": "http://file.hstatic.net/1000010797/file/hand-to-hand.png",
                "transfer_cod": True,
                "service_group_id": "4H"
            }
        ],
        "currency": "VND"
    },
    {
        "_id": "SGN-BDG-SAMEDAY",
        "set_idle_status_when_creating_order": True,
        "idle_timeout": 12000,
        "timeout": 4800,
        "commission_type": "PERCENTAGE",
        "require_to": True,
        "require_request": False,
        "rebroadcast_interval": 4800,
        "rebroadcast_limit": 12,
        "max_distance": 20000,
        "city_id": "SGN",
        "enable": True,
        "name": "4H BDG",
        "name_vi_vn": "4H BDG",
        "name_en_us": "4H BDG",
        "icon_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/aha-service/4H.jpg",
        "map_icon_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/core_services/xe1-02.png",
        "order": 4,
        "broadcast_distance": 2000,
        "advance_broadcast_distance": 5000,
        "stop_fee": 0,
        "cod": 500000,
        "max_cod": 1000000,
        "max_cod_per_stop_point": 1000000,
        "first_order_cod": 1,
        "description": "Giao hàng nội thành, cam kết trong 4 giờ*",
        "description_vi_vn": "Giao hàng nội thành, cam kết trong 4 giờ",
        "distance_fee": "0",
        "partner_distance_fee": "(27000 if x <= 10 else 36000 if x <= 15 else 42000 if x <= 20 else 42000 + (x-20) * 5500)",
        "commission_value": 0.212,
        "max_concurrent_orders": 4,
        "max_stop_points": 1,
        "fee_description_vi_vn": "Thời gian: tối đa 4 giờ (áp dụng đơn hàng dưới 20km)\n\nThời gian đặt đơn:\n- HN: 9:00-16:00\n- TP.HCM, Bình Dương: 9:00-17:00\n\nSố điểm giao tối đa: 1\n\nPhí quãng đường:\n+ 0-10km :27,000đ \n+ 10-15km:36,000đ\n+ 15-20km:42,000đ\n\nTrọng lượng tiêu chuẩn: 5kg\nKích thước tiêu chuẩn: 25x32x12\n\nMức COD tối đa: 1,000,000đ\nPhí COD: Miễn phí",
        "fee_description_en_us": "Leadtime: Maximum:4H\n(distance under 20km)\n\nMaximum drop off: 1\n\n\n\nDelivery time:\n- HN: 9:00-16:00 PM\n- TP.HCM, Bình Dương: 9:00-17:00 PM\n\nDistance fee:\n- From 0 - 10km: 27,000 VND\n- From 10 - 15km: 36,000 VND/km\n- From 15 - 20km: 42,000 VND/km\n\n\n\nPayload capacity: 5 kg\nSuitable goods (LxWxH): 25x32x12 cm\n\n\nMaximum COD: 1,000,000 VND \nCOD fee: Free",
        "description_en_us": "Giao hàng nội thành, cam kết trong 4 giờ",
        "planner_config": {
            "enable": True,
            "base_price": 22000,
            "epd_target": 6.2,
            "vehicle_capacity": 10,
            "idle_timeout": 3600,
            "outlier_service_id": "SGN-POOL",
            "dispatch_mode": "RECOMMEND",
            "matching_rate": 0.5,
            "matching_timeout": 0,
            "outlier_max_distance": 20000,
            "max_distance": 27000,
            "end_day_epd": 5.3,
            "stop_loss": 500000,
            "current_outlier_loss": 6026400
        },
        "opening_hours": "9-17",
        "cross_service": {
            "enable": True,
            "services": [
                "SGN-POOL"
            ]
        },
        "available_districts": [
            "VN.HC.QJ",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.QA",
            "VN.HC.QB",
            "VN.HC.QC",
            "VN.HC.QD",
            "VN.HC.QE",
            "VN.HC.QF",
            "VN.HC.QG",
            "VN.HC.QH",
            "VN.HC.QI"
        ],
        "delivery_type": "SAMEDAY",
        "notify_package_return": True,
        "parent_id": "",
        "uniform_verify": False,
        "service_hours": {
            "0": [
                {
                    "start_time": 540,
                    "end_time": 660
                },
                {
                    "start_time": 660,
                    "end_time": 780
                },
                {
                    "start_time": 780,
                    "end_time": 900
                },
                {
                    "start_time": 900,
                    "end_time": 1020
                }
            ],
            "1": [
                {
                    "start_time": 540,
                    "end_time": 660
                },
                {
                    "start_time": 660,
                    "end_time": 780
                },
                {
                    "start_time": 780,
                    "end_time": 900
                },
                {
                    "start_time": 900,
                    "end_time": 1020
                }
            ],
            "2": [
                {
                    "start_time": 540,
                    "end_time": 660
                },
                {
                    "start_time": 660,
                    "end_time": 780
                },
                {
                    "start_time": 780,
                    "end_time": 900
                },
                {
                    "start_time": 900,
                    "end_time": 1020
                }
            ],
            "3": [
                {
                    "start_time": 540,
                    "end_time": 660
                },
                {
                    "start_time": 660,
                    "end_time": 780
                },
                {
                    "start_time": 780,
                    "end_time": 900
                },
                {
                    "start_time": 900,
                    "end_time": 1020
                }
            ],
            "4": [
                {
                    "start_time": 540,
                    "end_time": 660
                },
                {
                    "start_time": 660,
                    "end_time": 780
                },
                {
                    "start_time": 780,
                    "end_time": 900
                },
                {
                    "start_time": 900,
                    "end_time": 1020
                }
            ],
            "5": [
                {
                    "start_time": 540,
                    "end_time": 660
                },
                {
                    "start_time": 660,
                    "end_time": 780
                },
                {
                    "start_time": 780,
                    "end_time": 900
                },
                {
                    "start_time": 900,
                    "end_time": 1020
                }
            ],
            "6": [
                {
                    "start_time": 540,
                    "end_time": 660
                },
                {
                    "start_time": 660,
                    "end_time": 780
                },
                {
                    "start_time": 780,
                    "end_time": 900
                },
                {
                    "start_time": 900,
                    "end_time": 1020
                }
            ]
        },
        "payment_method": [
            {
                "description": "Cash",
                "description_vi_vn": "Tiền mặt",
                "payment": "cash",
                "order": 1
            },
            {
                "description": "Balance",
                "description_vi_vn": "Ví AhaMove",
                "payment": "balance",
                "order": 2
            },
            {
                "description": "MoMo e-Wallet",
                "description_vi_vn": "Ví điện tử MoMo",
                "payment": "momo",
                "order": 3
            },
            {
                "description": "ZaloPay e-Wallet",
                "description_vi_vn": "Ví điện tử ZaloPay",
                "payment": "Zalopay",
                "order": 4
            }
        ],
        "enable_platform": [
            "momo_deeplink",
            "momo_permission",
            "zalo",
            "zalopay",
            "smartpay_deeplink",
            "viettel-pay_deeplink",
            "vpbank_deeplink"
        ],
        "group_name_en_us": "Tiết kiệm",
        "group_name_vi_vn": "Tiết kiệm",
        "vat_rate": 0.1,
        "priority_score": 6,
        "distance_fee_v3": {
            "blocks": [
                {
                    "from": 0,
                    "to": 100000,
                    "base": 0,
                    "price_multiplier": 0
                }
            ],
            "hour_rates": []
        },
        "group_id": "4H",
        "animated_url": "https://i.imgur.com/xiDxEYN.png",
        "requests": [
            {
                "_id": "SGN-BDG-SAMEDAY-TIP",
                "enable": True,
                "name": "Hỗ trợ tài xế",
                "name_vi_vn": "Hỗ trợ tài xế",
                "name_en_us": "Tipping",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/sr_tipping.png",
                "img_url": "http://file.hstatic.net/1000010797/file/tipping_final.jpg",
                "order": 4,
                "price": 5000,
                "max_input": 6,
                "no_commission": True,
                "description_vi_vn": "Hãy chọn dịch vụ này nếu bạn muốn hỗ trợ tài xế trong giờ cao điểm, khi cần giao hàng lên lầu, nơi phải tốn phí giữ xe, khi thời tiết khó khăn, hoặc đơn giản là muốn thưởng thêm cho tài xế. Ngoài ra, tính năng này sẽ giúp cho đơn hàng của bạn được ưu tiên hơn trong thời gian cao điểm.",
                "description_en_us": "This will show your support or compliment to the driver, especially in rush hours, hand to hand delivery, bad weather. Also, this feature will prioritize your request in peak time.",
                "type": "PER_UNIT",
                "description": "",
                "service_id": "SGN-BDG-SAMEDAY",
                "service_group_id": "4H",
                "group_id": "TIP"
            }
        ],
        "currency": "VND"
    },
    {
        "_id": "SGN-DG",
        "commission_type": "PERCENTAGE",
        "require_to": True,
        "require_request": False,
        "parent_id": "",
        "city_id": "SGN",
        "name": "Đồng giá 25",
        "name_vi_vn": "Đồng giá 25",
        "name_en_us": "Đồng giá 25",
        "cancel_timeout": 60,
        "tooltips": {
            "ASSIGNING": {
                "message": [
                    "Your order has been confirmed.",
                    "Note: You can only cancel this order within 60 seconds"
                ],
                "message_vi_vn": [
                    "Đơn hàng của bạn đã được AhaMove xác nhận.",
                    "Lưu ý: Bạn chỉ có thể huỷ đơn hàng trong vòng 60 giây"
                ]
            }
        },
        "min_stop_points": 4,
        "max_stop_points": 10,
        "map_icon_url": "https://ahamove.com/wp-content/uploads/2019/01/icon-Tet.png",
        "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/sp-same-price.png",
        "order": 5,
        "broadcast_distance": 3000,
        "advance_broadcast_distance": 3000,
        "stop_fee": 25000,
        "timeout": 1800,
        "distance_fee": "25000 if x <= 25 else 25000 + (x - 25) * 10000",
        "cod": 10000000,
        "first_order_cod": 1,
        "max_concurrent_orders": 2,
        "enable": True,
        "commission_value": 0.236,
        "rebroadcast_interval": 1200,
        "fee_description_en_us": "Stop point fee: đ25,000/stop point \nDistance fee:\n+ First 25km: Free\n+ Above 25km: đ10,000/km\n\n* VAT included\n* Minimum stop points per order: 04",
        "description_en_us": "Save 50% - Delivery within 4h guaranteed",
        "description_vi_vn": "Tiết kiệm 50%, giao hàng dưới 4 tiếng.",
        "fee_description_vi_vn": "Phí điểm giao: đ25.000/điểm\nPhí quãng đường:\n+ 25km đầu: Miễn phí\n+ Trên 25km: đ10.000/km\n\n* Giá đã bao gồm VAT\n* Số điểm giao tối thiểu: 04 điểm",
        "supplier_description": "https://ahamove.com/quy-trinh-nhan-don-dong-gia-25/",
        "notify_package_return": True,
        "pending_period": 60,
        "cross_service": {
            "enable": False,
            "services": []
        },
        "cross_city": {
            "enable": True,
            "cities": [
                "SGN"
            ]
        },
        "available_districts": [
            "VN.HC.NB",
            "VN.HC.CG",
            "VN.HC.CC",
            "VN.HC.BC",
            "VN.HC.HM",
            "VN.TDM",
            "VN.TA",
            "VN.DA",
            "VN.HC.QB",
            "VN.HC.QC",
            "VN.HC.QG",
            "VN.HC.BH",
            "VN.HC.GV",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.PN",
            "VN.HC.QJ",
            "VN.HC.QD",
            "VN.HC.BT",
            "VN.HC.QF",
            "VN.HC.QA",
            "VN.HC.QE",
            "VN.HC.TB",
            "VN.HC.TD",
            "VN.HC.QH",
            "VN.HC.QI",
            "VN.HC.TP"
        ],
        "rebroadcast_limit": 1,
        "uniform_verify": True,
        "uniform_verify_message_en_us": "Is your driver wearing proper uniform (including AhaMove's jacket, helmet)?",
        "uniform_verify_message_vi_vn": "Tài xế có mang đồng phục (áo, nón) hay không?",
        "max_cod": 10000000,
        "group_name_en_us": "Budget delivery",
        "group_name_vi_vn": "Tiết kiệm",
        "priority_score": 6,
        "distance_fee_v3": {
            "blocks": [
                {
                    "from": 0,
                    "to": 25,
                    "base": 25000,
                    "price_multiplier": 0
                },
                {
                    "from": 25,
                    "to": 100000,
                    "base": 25000,
                    "price_multiplier": 10000
                }
            ],
            "hour_rates": []
        },
        "group_id": "OTHERS",
        "animated_url": "https://i.imgur.com/xiDxEYN.png",
        "requests": [
            {
                "_id": "SGN-DG-TIP",
                "name": "Hỗ trợ tài xế",
                "enable": True,
                "name_vi_vn": "Hỗ trợ tài xế",
                "name_en_us": "Tipping",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/sr_tipping.png",
                "img_url": "http://file.hstatic.net/1000010797/file/tipping_final.jpg",
                "order": 1,
                "price": 5000,
                "max_input": 6,
                "no_commission": True,
                "description_vi_vn": "Hãy chọn dịch vụ này nếu bạn muốn hỗ trợ tài xế trong giờ cao điểm, khi cần giao hàng lên lầu, nơi phải tốn phí giữ xe, khi thời tiết khó khăn, hoặc đơn giản là muốn thưởng thêm cho tài xế. Ngoài ra, tính năng này sẽ giúp cho đơn hàng của bạn được ưu tiên hơn trong thời gian cao điểm.",
                "description_en_us": "This will show your support or compliment to the driver, especially in rush hours, hand to hand delivery, bad weather. Also, this feature will prioritize your request in peak time.",
                "type": "PER_UNIT",
                "description": "",
                "service_id": "SGN-DG",
                "group_id": "TIP",
                "service_group_id": "OTHERS"
            },
            {
                "_id": "SGN-DG-ROUND-TRIP",
                "name": "Quay lại điểm lấy hàng",
                "enable": True,
                "name_vi_vn": "Quay lại điểm lấy hàng",
                "name_en_us": "Return to pick up location",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_round_trip.png",
                "img_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_round_trip.png",
                "order": 2,
                "price": 25000,
                "description_vi_vn": "Tài xế sẽ quay lại điểm lấy hàng với số phí bằng 25,000vnd",
                "description_en_us": "Driver will return to the pick-up location with the fee of 25,000vnd",
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-DG",
                "supplier_description": "Tài xế sẽ quay lại điểm lấy hàng với số phí bằng 80% phí khoảng cách. Lưu ý: Phí khoảng cách là số phí dựa theo số km vận chuyển, ko bao gồm phí điểm dừng và các loại phí khác.",
                "group_id": "TRIP",
                "service_group_id": "OTHERS"
            }
        ],
        "currency": "VND"
    },
    {
        "_id": "SGN-INTERCT-GHN",
        "commission_type": "PERCENTAGE",
        "first_order_cod": 1,
        "city_id": "SGN",
        "broadcast_distance": 3000,
        "enable": True,
        "partner": True,
        "timeout": 432000,
        "name": "Giao hàng liên tỉnh",
        "name_vi_vn": "Giao hàng liên tỉnh",
        "name_en_us": "Giao hàng liên tỉnh",
        "icon_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/services/nationwide_service.png",
        "map_icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/tv_motorcycle.png",
        "order": 5,
        "stop_fee": 0,
        "distance_fee": "0",
        "commission_value": 0.2,
        "parent_id": "",
        "require_to": True,
        "max_distance": 2000000,
        "delivery_type": "NATIONWIDE",
        "partner_service_id": "53320",
        "advance_broadcast_distance": 0,
        "cross_service": {
            "enable": True,
            "services": []
        },
        "max_stop_points": 6,
        "not_available_drop_off_districts": [
            "VN.HC.CG",
            "VN.HC.TD",
            "VN.HC.QJ",
            "VN.HC.QK",
            "VN.HC.QG",
            "VN.HC.BH",
            "VN.HC.QF",
            "VN.HC.QB",
            "VN.HC.QI",
            "VN.HC.TP",
            "VN.HC.TB",
            "VN.HC.QA",
            "VN.HC.PN",
            "VN.HC.BT",
            "VN.HC.GV",
            "VN.HC.HM",
            "VN.HC.QH",
            "VN.HC.QE",
            "VN.HC.QC",
            "VN.HC.CC",
            "VN.HC.QD",
            "VN.HC.NB",
            "VN.HC.QL",
            "VN.HC.BC"
        ],
        "note": "106.663631,10.769553",
        "service_hours": {},
        "max_cod": 30000000,
        "payment_method": [
            {
                "description": "Balance",
                "description_vi_vn": "Ví AhaMove",
                "payment": "balance",
                "order": 3
            },
            {
                "description": "Cash",
                "description_vi_vn": "Tiền mặt",
                "payment": "cash",
                "order": 3
            }
        ],
        "priority_score": 6,
        "distance_fee_v3": {
            "blocks": [
                {
                    "from": 0,
                    "to": 100000,
                    "base": 0,
                    "price_multiplier": 0
                }
            ],
            "hour_rates": []
        },
        "group_id": "INTERCT",
        "animated_url": "https://i.imgur.com/xiDxEYN.png",
        "requests": [
            {
                "_id": "GHN-INSURANCE",
                "name": "Bảo hiểm",
                "enable": True,
                "name_vi_vn": "Khai giá hàng ",
                "name_en_us": "Declare-item-cost",
                "icon_url": "as",
                "img_url": "sdas",
                "order": 2,
                "description_vi_vn": "asd as",
                "description_en_us": "as das",
                "type": "COMMISSION_PERCENTAGE",
                "price": 0.1,
                "description": "",
                "service_id": "SGN-INTERCT-GHN",
                "service_group_id": "GHN"
            }
        ],
        "currency": "VND"
    },
    {
        "_id": "SGN-TRUCK-500",
        "enable": True,
        "order": 5,
        "city_id": "SGN",
        "name": "Xe tải 500kg",
        "rebroadcast_interval": 1200,
        "rebroadcast_limit": 3,
        "name_vi_vn": "Xe tải 500kg",
        "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/services/truck/Truck-500.png",
        "map_icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/services/Truck_service_map_icon/Truck.png",
        "parent_id": "SGN-TRUCK",
        "stop_fee": 11000,
        "commission_type": "PERCENTAGE",
        "commission_value": 0.212,
        "distance_fee": "185000 if x <= 4 else 185000 + (x - 4) * 22000 if x <= 10 else 185000 + 6 * 22000 + (x - 10) * 16000 if x <= 15 else 185000 + 6 * 22000 + 5 * 16000  + (x - 15) * 15500",
        "vat_rate": 0.1,
        "require_to": True,
        "broadcast_distance": 50000,
        "name_en_us": "Truck 500kg",
        "max_stop_points": 5,
        "max_cod": 5000000,
        "enable_platform": [
            "momo_deeplink",
            "momo_permission",
            "zalo",
            "zalopay",
            "smartpay_deeplink",
            "VIETTEL",
            "onwheel"
        ],
        "cross_service": {
            "enable": True,
            "services": [
                "SGN-TRUCK-2000"
            ]
        },
        "max_concurrent_orders": 5,
        "is_recommend": False,
        "delivery_type": "TRUCK",
        "notify_package_return": True,
        "description_en_us": "📦 (LxWxH) 1.4 x 1.4 x 1 meters",
        "description_vi_vn": "📦 (DxRxC) 1.4 x 1.4 x 1 mét",
        "fee_description_vi_vn": "Khối lượng chuyên chở: 500kg\nHàng hoá phù hợp (DxRxC): 1.4 x 1.4 x 1 mét\n\nPhí quãng đường:\n- Từ 00 - 04km: 185,000đ\n- Từ 04 - 10km: 20,000đ/km\n- Từ 10 - 15km: 14,375đ/km\n- Trên 15km: 14,000đ/km\n\nKhung giờ cấm tải (Nội thành)\n- Từ 06:00 - 09:00 AM\n- Từ 16:00 - 20:00 PM\n*Mách bạn: Hãy sử dụng xe tải VAN trong khung giờ cấm tải để tối ưu đơn hàng\n\nMức COD tối đa: 10,000,000đ\nPhí COD:\n- COD <   2,000,000đ: Miễn phí\n- COD >= 2,000,000đ: 0.8% x Giá trị COD",
        "fee_description_en_us": "Payload capacity: 500kg\nSuitable goods (LxWxH): 1.4 x 1.4 x 1 meters\n\nDistance fee:\n- From 00 - 04km: 185,000 VND\n- From 04 - 10km: 20,000 VND/km\n- From 10 - 15km: 14,375 VND/km\n- Over 15km: 14,000 VND/km\n\nTruck ban hours (Urban areas)\n- From 06:00 - 09:00 AM\n- From 16:00 - 20:00 PM\n*Tip: Use VAN during truck ban hours to optimize orders\n\nMaximum COD: 10,000,000 VND\nCOD fee:\n- COD <   2,000,000 VND: Free\n- COD >= 2,000,000 VND: 0.8% x Value of COD",
        "group_name_en_us": "Large parcel delivery",
        "group_name_vi_vn": "Hàng hóa kích thước lớn",
        "auto_assign": True,
        "recommendation_config": {
            "supplier_timeout": 30,
            "recommend_timeout": 90,
            "recommend_radius": 3500,
            "sleep_interval": 90,
            "dispatch_mode": "RECOMMEND",
            "pool_mode": "NO_POOL",
            "pool_saving_threshold": 0.2,
            "poolable": False
        },
        "vehicle_info": {
            "image": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/services/truck/Truck-500.png",
            "length": 1.4,
            "width": 1.4,
            "height": 1.2,
            "weight": 500.0,
            "box_volume": 10,
            "short_intro_vi": "Thích hợp cho hàng hoá nhỏ và không hoạt động trong khung giờ cấm tải ",
            "short_intro_en": "This vehicle is suitable to carry small parcels and deactive in truck ban hours",
            "short_description_vi": "1.4 x 1.4 x 1.0 mét. Lên tới 500kg",
            "short_description_en": "1.4 x 2.4 x 1.0 Meter. Up to 500kgs",
            "description_vi_vn": "Khối lượng chuyên chở: 500kg\nHàng hoá phù hợp (DxRxC): 1.6 x 1.4 x 1.2  mét\n\nPhí quãng đường:\n- Từ 00 - 04km: 185,000đ\n- Từ 04 - 10km: 20,000đ/km\n- Từ 10 - 15km: 14,375đ/km\n- Trên 15km: 14,000đ/km\n\nMức COD tối đa: 10,000,000đ\nPhí COD:\n- COD <   2,000,000đ: Miễn phí\n- COD >= 2,000,000đ: 0.8% x Giá trị COD",
            "description_en_us": "Payload capacity: 500kg\nSuitable goods (LxWxH): 1.6 x 1.4 x 1.2 meters\n\nDistance fee:\n- From 00 - 04km: 185,000 VND\n- From 04 - 10km: 20,000 VND/km\n- From 10 - 15km: 14,375 VND/km\n- Over 15km: 14,000 VND/km\n\nMaximum COD: 10,000,000 VND\nCOD fee:\n- COD <   2,000,000 VND: Free\n- COD >= 2,000,000 VND: 0.8% x Value of COD"
        },
        "distance_fee_v3": {
            "blocks": [
                {
                    "from": 0,
                    "to": 4,
                    "base": 185000,
                    "price_multiplier": 0
                },
                {
                    "from": 4,
                    "to": 10,
                    "base": 185000,
                    "price_multiplier": 22000
                },
                {
                    "from": 10,
                    "to": 15,
                    "base": 317000,
                    "price_multiplier": 16000
                },
                {
                    "from": 15,
                    "to": 100000,
                    "base": 397000,
                    "price_multiplier": 15500
                }
            ],
            "hour_rates": []
        },
        "timeout": 120001,
        "available_districts": [
            "VN.HC.BC",
            "VN.HC.NB",
            "VN.TP",
            "VN.HC.BH",
            "VN.HC.BT",
            "VN.HC.GV",
            "VN.HC.PN",
            "VN.HC.QJ",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.QA",
            "VN.HC.QB",
            "VN.HC.QC",
            "VN.HC.QD",
            "VN.HC.QE",
            "VN.HC.QF",
            "VN.HC.QG",
            "VN.HC.QH",
            "VN.HC.QI",
            "VN.HC.TB",
            "VN.HC.TD"
        ],
        "opening_hours": "0-24",
        "enable_cancellation_punishment": False,
        "truck_ban": {
            "ban_districts": [
                {
                    "_id": 260,
                    "hasc_2": "VN.HC.BH",
                    "name_2": "Bình Thạnh",
                    "city_id": "SGN",
                    "name": "BH",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 26
                },
                {
                    "_id": 267,
                    "hasc_2": "VN.HC.PN",
                    "name_2": "Phú Nhuận",
                    "city_id": "SGN",
                    "name": "PN",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 29
                },
                {
                    "_id": 268,
                    "hasc_2": "VN.HC.QJ",
                    "name_2": "Quận 10",
                    "city_id": "SGN",
                    "name": "QJ",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 30
                },
                {
                    "_id": 269,
                    "hasc_2": "VN.HC.QK",
                    "name_2": "Quận 11",
                    "city_id": "SGN",
                    "name": "QK",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 31
                },
                {
                    "_id": 270,
                    "hasc_2": "VN.HC.QL",
                    "name_2": "Quận 12",
                    "city_id": "SGN",
                    "name": "QL",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 32
                },
                {
                    "_id": 271,
                    "hasc_2": "VN.HC.QA",
                    "name_2": "Quận 1",
                    "city_id": "SGN",
                    "name": "QA",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 33
                },
                {
                    "_id": 273,
                    "hasc_2": "VN.HC.QC",
                    "name_2": "Quận 3",
                    "city_id": "SGN",
                    "name": "QC",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 35
                },
                {
                    "_id": 274,
                    "hasc_2": "VN.HC.QD",
                    "name_2": "Quận 4",
                    "city_id": "SGN",
                    "name": "QD",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 36
                },
                {
                    "_id": 275,
                    "hasc_2": "VN.HC.QE",
                    "name_2": "Quận 5",
                    "city_id": "SGN",
                    "name": "QE",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 37
                },
                {
                    "_id": 276,
                    "hasc_2": "VN.HC.QF",
                    "name_2": "Quận 6",
                    "city_id": "SGN",
                    "name": "QF",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 38
                },
                {
                    "_id": 277,
                    "hasc_2": "VN.HC.QG",
                    "name_2": "Quận 7",
                    "city_id": "SGN",
                    "name": "QG",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 39
                },
                {
                    "_id": 278,
                    "hasc_2": "VN.HC.QH",
                    "name_2": "Quận 8",
                    "city_id": "SGN",
                    "name": "QH",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 40
                },
                {
                    "_id": 280,
                    "hasc_2": "VN.HC.TB",
                    "name_2": "Tân Bình",
                    "city_id": "SGN",
                    "name": "TB",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 42
                }
            ],
            "recommend_service": "SGN-TRUCK-1000",
            "enable": True,
            "ban_hours": [
                {
                    "from": 22,
                    "to": 23
                },
                {
                    "from": 16,
                    "to": 17
                }
            ]
        },
        "map_icon_3d": {
            "url": "https://firebasestorage.googleapis.com/v0/b/aha-chat-292008.appspot.com/o/3dicon%2Ftruck-500.png?alt=media&token=c11b2e4e-1dfb-46aa-9d76-8574e234a001",
            "sprite_size": 64,
            "sprite_count": 64
        },
        "priority_score": 6,
        "assigning_before": [
            {
                "from": 0,
                "to": 7,
                "value": 10800
            },
            {
                "from": 16,
                "value": 3600,
                "to": 18
            },
            {
                "from": 18,
                "to": 20,
                "value": 400
            },
            {
                "from": 20,
                "to": 23,
                "value": 1000
            }
        ],
        "alternative_vehicles": [
            "TRUCK-1000",
            "TRUCK-1500",
            "TRUCK-2000",
            "VAN-500",
            "VAN-1000",
            "PICKUP-TRUCK"
        ],
        "default_vehicles": [
            "TRUCK-500"
        ],
        "is_select_vehicle_allowed": True,
        "max_item_value": 30000000.0,
        "group_id": "TRUCK-500",
        "animated_url": "https://i.imgur.com/xiDxEYN.png",
        "requests": [
            {
                "_id": "SGN-TRUCK-500-BOCXEP-KLLMC",
                "name": "Bốc xếp không lên lầu - 1 chiều",
                "name_vi_vn": "Bốc xếp không lên lầu - 1 chiều",
                "name_en_us": "1 Way moving help (ground floor only)",
                "icon_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_loading_per_helper.png",
                "img_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_loading_per_helper.png",
                "order": 1,
                "price": 50000,
                "description_vi_vn": "Tài xế hỗ trợ bốc xếp hàng hóa (đã được đóng thùng) xuống xe đến địa điểm chỉ định trong vòng 100m HOẶC ngược lại (Áp dụng cho 1 lượt và không lên lầu). Các trường hợp phát sinh thêm, vui lòng thoả thuận với tài xế.",
                "description_en_us": "Driver provides moving help (already packaged) from vehicle to designated location within 100m OR vice versa (Apply for 1 turn and ground floor only). For additional cases, please negotiate with the driver.",
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-TRUCK-500",
                "enable": True,
                "category": "UNLOADING",
                "service_group_id": "TRUCK-500",
                "group_id": "BOCXEP"
            },
            {
                "_id": "SGN-TRUCK-500-CHUYENNHA",
                "name": "Gói hỗ trợ chuyển nhà cơ bản",
                "name_vi_vn": "Gói hỗ trợ chuyển nhà cơ bản",
                "name_en_us": "Gói hỗ trợ chuyển nhà cơ bản",
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/house-moving_s.png",
                "order": 1,
                "price": 300000,
                "description_vi_vn": "Chi tiết gói: \n- Hỗ trợ bốc xếp: 240000\n- Phí chờ: 60000\n \n Lưu ý: \n- Địa hình vận chuyển: Không quá 100m và 2 tầng/ lầu tại 2 chiều.\n- Vui lòng tháo lắp đồ điện lạnh, nội thất và đóng gói hàng hoá trước khi đặt dịch vụ\n- Trường hợp có phát sinh cước luân chuyển, bốc xếp vui lòng liên hệ tổng đài 1900545411 để được xác nhận.",
                "description_en_us": "Chi tiết gói: \n- Hỗ trợ bốc xếp: 240000\n- Phí chờ: 60000\n \n Lưu ý: \n- Địa hình vận chuyển: Không quá 100m và 2 tầng/ lầu tại 2 chiều.\n- Vui lòng tháo lắp đồ điện lạnh, nội thất và đóng gói hàng hoá trước khi đặt dịch vụ\n- Trường hợp có phát sinh cước luân chuyển, bốc xếp vui lòng liên hệ tổng đài 1900545411 để được xác nhận.",
                "type": "BOOLEAN",
                "description": "Chi tiết gói: \n- Hỗ trợ bốc xếp: 240000\nPhí chờ: 60000\n \n Lưu ý: \n- Địa hình vận chuyển: Không quá 100m và 2 tầng/ lầu tại 2 chiều.\n- Vui lòng tháo lắp đồ điện lạnh, nội thất và đóng gói hàng hoá trước khi đặt dịch vụ\n- Trường hợp có phát sinh cước luân chuyển, bốc xếp vui lòng liên hệ tổng đài 1900545411 để được xác nhận.",
                "service_id": "SGN-TRUCK-500",
                "img_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/house-moving.png",
                "enable": True,
                "options": [
                    {
                        "code": "ITEM_1",
                        "name_vi_vn": "Hỗ trợ bốc xếp",
                        "name_en_us": "Hỗ trợ bốc xếp",
                        "selectable": True
                    },
                    {
                        "code": "ITEM_2",
                        "name_vi_vn": "Phí chờ",
                        "name_en_us": "Phí chờ",
                        "selectable": True
                    },
                    {
                        "code": "ITEM_3",
                        "name_vi_vn": "Combo Bốc xếp và phí chờ",
                        "name_en_us": "Combo Bốc xếp và phí chờ",
                        "selectable": True
                    }
                ],
                "service_group_id": "TRUCK-500",
                "group_id": "CHUYENNHA"
            },
            {
                "_id": "SGN-TRUCK-500-INSURANCE",
                "name": "Khai giá hàng hoá",
                "name_vi_vn": "Khai giá hàng hoá",
                "name_en_us": "Value declaration",
                "enable": True,
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/Insurance/secure+24x24%402x.png",
                "order": 1,
                "device_types": [
                    "web",
                    "android",
                    "ios"
                ],
                "price_blocks": [
                    {
                        "from": 0,
                        "to": 10000001,
                        "price": 2000,
                        "description_vi_vn": "Bồi thường mất mát hoặc hư hỏng theo giá trị hàng hoá của bạn",
                        "description_en_us": "Coverage for loss or damage according to the value of your items"
                    }
                ],
                "no_supplier_payout": True,
                "type": "COD_INSURANCE",
                "applied_stp_num": 10,
                "max_item_value": 10000000,
                "service_id": "SGN-TRUCK-500",
                "description_url": "https://ahamove.com/phi-khai-gia-cho-truck-ahmxsaladin/",
                "benefit_url": "https://ahamove.com/phi-khai-gia-cho-truck-ahmxsaladin/",
                "non_cod_description": "Bồi thường mất mát hoặc hư hỏng theo danh mục hàng hoá của bạn",
                "none_cod_price_blocks": {
                    "electronics": 2000,
                    "health & beauty": 2000,
                    "housing & lifestyle": 2000,
                    "food": 2000,
                    "mother & baby": 2000,
                    "fashion": 2000,
                    "grocery": 2000,
                    "restaurant": 2000,
                    "sport": 2000,
                    "drink": 2000,
                    "other": 2000,
                    "individual needs": 2000,
                    "transportation": 2000
                },
                "service_group_id": "TRUCK-500",
                "required_item_value": True
            },
            {
                "_id": "SGN-TRUCK-500-BOCXEP",
                "name": "Bốc xếp",
                "enable": True,
                "support_remarks": True,
                "name_vi_vn": "Bốc xếp",
                "name_en_us": "Unloading",
                "icon_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/Special+Request/Special+Request+Icon/Bulky_packages.jpg",
                "order": 1,
                "tier_list": [
                    {
                        "code": "TIER_1",
                        "name_vi_vn": "Bốc xếp không lên lầu - 1 chiều",
                        "name_en_us": "1 Way moving help (ground floor only)",
                        "selectable": True,
                        "price": 55000,
                        "description_vi_vn": "Tài xế hỗ trợ bốc xếp hàng hóa (đã được đóng thùng) xuống xe đến địa điểm chỉ định trong vòng 100m HOẶC ngược lại (Áp dụng cho 1 lượt và không lên lầu). Các trường hợp phát sinh thêm, vui lòng thoả thuận với tài xế.",
                        "description_en_us": "Driver provides moving help (already packaged) from vehicle to designated location within 100m OR vice versa (Apply for 1 turn and ground floor only). For additional cases, please negotiate with the driver.",
                        "img_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_loading_per_helper.png"
                    },
                    {
                        "code": "TIER_2",
                        "name_vi_vn": "Mức 1",
                        "name_en_us": "Package 1",
                        "price": 77000,
                        "selectable": True,
                        "description_vi_vn": "Tài xế hỗ trợ bốc xếp hàng hóa (đã được đóng thùng) xuống xe đến địa điểm chỉ định trong vòng 100m VÀ ngược lại (Áp dụng cho 2 lượt và không lên lầu). Các trường hợp phát sinh thêm, vui lòng thoả thuận với tài xế.",
                        "description_en_us": "Driver provides moving help (already packaged) from vehicle to designated location within 100m AND vice versa (Apply for 2 turns and ground floor only). For additional cases, please negotiate with the driver.",
                        "img_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_loading_per_helper.png"
                    },
                    {
                        "code": "TIER_3",
                        "name_vi_vn": "Bốc xếp tại nhà có lầu - 1 chiều",
                        "name_en_us": "1 Way moving help (Maximum 1 Floor)",
                        "selectable": True,
                        "price": 110000,
                        "description_vi_vn": "Tài xế hỗ trợ bốc xếp hàng hóa (đã được đóng thùng) xuống xe đến địa điểm chỉ định trong vòng 100m HOẶC ngược lại (Áp dụng cho 1 lượt, 1 lầu). Các trường hợp phát sinh thêm, vui lòng thoả thuận với tài xế.",
                        "description_en_us": "Driver provides moving help (already packaged) from vehicle to designated location within 100m OR vice versa (Apply for 1 turn and maximum 1 floor). For additional cases, please negotiate with the driver.",
                        "img_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_moving_help_upstair.png"
                    },
                    {
                        "code": "TIER_4",
                        "name_vi_vn": "Bốc xếp tại nhà có lầu - 2 chiều",
                        "name_en_us": "2 Ways moving help (Maximum 1 Floor)",
                        "selectable": True,
                        "price": 165000,
                        "description_vi_vn": "Tài xế hỗ trợ bốc xếp hàng hóa (đã được đóng thùng) xuống xe đến địa điểm chỉ định trong vòng 100m VÀ ngược lại (Áp dụng cho 2 lượt, 1 lầu). Các trường hợp phát sinh thêm, vui lòng thoả thuận với tài xế.",
                        "description_en_us": "Driver provides moving help (already packaged) from vehicle to designated location within 100m AND vice versa (Apply for 1 turn and maximum 1 floor). For additional cases, please negotiate with the driver.",
                        "img_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_moving_help_upstair.png"
                    }
                ],
                "type": "TIER",
                "service_id": "SGN-TRUCK-500",
                "img_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_moving_help_upstair.png",
                "description_vi_vn": "Tài xế hỗ trợ bốc xếp",
                "supplier_description_url": "https://ahamove.com/giao-hang-cong-kenh",
                "service_group_id": "TRUCK-500",
                "group_id": "BOCXEP"
            },
            {
                "_id": "SGN-TRUCK-500-TRANSFER-COD",
                "name": "Thu hộ qua ví điện tử (new)",
                "enable": True,
                "transfer_cod": False,
                "support_remarks": True,
                "name_vi_vn": "Thu hộ qua ví điện tử (new)",
                "name_en_us": "Collect payment via e-wallet (new)",
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/icon-POD-extraservice.png",
                "order": 1,
                "price": 0,
                "no_commission": True,
                "type": "BOOLEAN",
                "service_id": "SGN-TRUCK-500",
                "img_url": "http://file.hstatic.net/1000010797/file/hand-to-hand.png",
                "description_vi_vn": "Tài xế không cần ứng trước tiền thu hộ. Người nhận chỉ cần quét mã QR để thanh toán qua ví điện tử hoặc ứng dụng Mobile Banking khi tài xế đến giao hàng. Tiền thu hộ sẽ tự động chuyển vào tài khoản COD của bạn sau khi đơn hàng hoàn tất.",
                "description_en_us": "Your driver doesn't have to pay in advance. Upon delivery, the recipient scans a QR code to pay via an e-wallet or Mobile Banking app. Payment will be transferred to your COD account once the order is complete.",
                "service_group_id": "TRUCK-500",
                "subtype": "epayment_on_delivery"
            },
            {
                "_id": "SGN-TRUCK-500-BOCXEP-KLLHC",
                "name": "Bốc xếp không lên lầu - 2 chiều",
                "name_vi_vn": "Bốc xếp không lên lầu - 2 chiều",
                "name_en_us": "2 Ways moving help (ground floor only)",
                "icon_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_loading_per_helper.png",
                "img_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_loading_per_helper.png",
                "order": 2,
                "price": 77000,
                "description_vi_vn": "Tài xế hỗ trợ bốc xếp hàng hóa (đã được đóng thùng) xuống xe đến địa điểm chỉ định trong vòng 100m VÀ ngược lại (Áp dụng cho 2 lượt và không lên lầu). Các trường hợp phát sinh thêm, vui lòng thoả thuận với tài xế.",
                "description_en_us": "Driver provides moving help (already packaged) from vehicle to designated location within 100m AND vice versa (Apply for 2 turns and ground floor only). For additional cases, please negotiate with the driver.",
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-TRUCK-500",
                "enable": True,
                "category": "UNLOADING",
                "service_group_id": "TRUCK-500",
                "group_id": "BOCXEP"
            },
            {
                "_id": "SGN-TRUCK-500-LOADERS",
                "name": "Thêm người bốc xếp",
                "enable": True,
                "name_vi_vn": "Thêm người bốc xếp",
                "name_en_us": "Thêm người bốc xếp",
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/more-pickers.png",
                "img_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/more-pickers.png",
                "order": 2,
                "price": 300000,
                "max_input": 3,
                "description_vi_vn": "Hàng hoá số lượng lớn hay có kích thước cồng kềnh, nặng và yêu cầu phải có 2 người bưng trở lên",
                "no_commission": False,
                "description_en_us": "Hàng hoá số lượng lớn hay có kích thước cồng kềnh, nặng và yêu cầu phải có 2 người bưng trở lên",
                "type": "PER_UNIT",
                "description": "Hàng hoá số lượng lớn hay có kích thước cồng kềnh, nặng và yêu cầu phải có 2 người bưng trở lên",
                "service_id": "SGN-TRUCK-500",
                "service_group_id": "TRUCK-500",
                "group_id": "LOADER"
            },
            {
                "_id": "SGN-TRUCK-500-BOCXEP-LLMC",
                "name": "Bốc xếp tại nhà có lầu - 1 chiều",
                "name_vi_vn": "Bốc xếp tại nhà có lầu - 1 chiều",
                "enable": True,
                "name_en_us": "1 Way moving help (Maximum 1 Floor)",
                "icon_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_moving_help_upstair.png",
                "img_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_moving_help_upstair.png",
                "order": 3,
                "price": 110000,
                "description_vi_vn": "Tài xế hỗ trợ bốc xếp hàng hóa (đã được đóng thùng) xuống xe đến địa điểm chỉ định trong vòng 100m HOẶC ngược lại (Áp dụng cho 1 lượt, 1 lầu). Các trường hợp phát sinh thêm, vui lòng thoả thuận với tài xế.",
                "description_en_us": "Driver provides moving help (already packaged) from vehicle to designated location within 100m OR vice versa (Apply for 1 turn and maximum 1 floor). For additional cases, please negotiate with the driver.",
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-TRUCK-500",
                "category": "UNLOADING",
                "service_group_id": "TRUCK-500",
                "group_id": "BOCXEP"
            },
            {
                "_id": "SGN-TRUCK-500-BOCXEP-LLHC",
                "name": "Bốc xếp tại nhà có lầu - 2 chiều",
                "name_vi_vn": "Bốc xếp tại nhà có lầu - 2 chiều",
                "name_en_us": "2 Ways moving help (Maximum 1 Floor)",
                "icon_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_moving_help_upstair.png",
                "img_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_moving_help_upstair.png",
                "order": 4,
                "price": 165000,
                "description_vi_vn": "Tài xế hỗ trợ bốc xếp hàng hóa (đã được đóng thùng) xuống xe đến địa điểm chỉ định trong vòng 100m VÀ ngược lại (Áp dụng cho 2 lượt, 1 lầu). Các trường hợp phát sinh thêm, vui lòng thoả thuận với tài xế.",
                "description_en_us": "Driver provides moving help (already packaged) from vehicle to designated location within 100m AND vice versa (Apply for 1 turn and maximum 1 floor). For additional cases, please negotiate with the driver.",
                "enable": True,
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-TRUCK-500",
                "category": "UNLOADING",
                "service_group_id": "TRUCK-500",
                "group_id": "BOCXEP"
            },
            {
                "_id": "SGN-TRUCK-500-ROUND-TRIP",
                "name": "Quay lại điểm lấy hàng",
                "enable": True,
                "name_vi_vn": "Quay lại điểm lấy hàng",
                "name_en_us": "Return to pick up location",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_round_trip.png",
                "img_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_round_trip.png",
                "order": 5,
                "description_vi_vn": "Tài xế sẽ quay lại điểm lấy hàng với cước phí bằng 50% phí khoảng cách. Lưu ý: Phí khoảng cách là cước phí dựa theo số km vận chuyển, không bao gồm phí điểm dừng và các loại phí khác.",
                "description_en_us": "Driver will return to pick up location for 50% of distance fee. Note: Distance fee is calculated solely by the travel distance, it does not include stop fee and others fee",
                "type": "COMMISSION_DISTANCE_PERCENTAGE",
                "price": 0.5,
                "description": "",
                "service_id": "SGN-TRUCK-500",
                "service_group_id": "TRUCK-500",
                "group_id": "ROUND-TRIP"
            }
        ],
        "currency": "VND"
    },
    {
        "_id": "SGN-2H-PUBLIC",
        "set_idle_status_when_creating_order": True,
        "idle_timeout": 300,
        "timeout": 1800,
        "commission_type": "PERCENTAGE",
        "require_to": True,
        "require_request": False,
        "rebroadcast_interval": 1200,
        "rebroadcast_limit": 48,
        "max_distance": 100000,
        "city_id": "SGN",
        "enable": True,
        "name": "2H PUBLIC",
        "name_vi_vn": "2H",
        "name_en_us": "2H",
        "icon_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/aha-service/2h.png",
        "map_icon_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/core_services/xe1-02.png",
        "order": 5,
        "broadcast_distance": 10000,
        "advance_broadcast_distance": 20000,
        "stop_fee": 4400,
        "max_cod": 1000000,
        "max_cod_per_stop_point": 1000000,
        "first_order_cod": 1,
        "distance_fee": "0",
        "partner_distance_fee": "(20000 if x <= 4 else 20000 + (x - 4) * 4400)",
        "commission_value": 0.212,
        "max_concurrent_orders": 4,
        "max_stop_points": 1,
        "planner_config": {
            "enable": True,
            "base_price": 22000,
            "epd_target": 6.16,
            "vehicle_capacity": 3,
            "idle_timeout": 900,
            "grocery_idle_timeout": 900,
            "outlier_service_id": "SGN-POOL",
            "dispatch_mode": "RECOMMEND",
            "matching_rate": 0.5,
            "matching_timeout": 0,
            "max_distance": 30000,
            "current_stop_loss": 0,
            "end_day_epd": 4.5,
            "stop_loss": 1000000000,
            "current_outlier_loss": 24000,
            "parent_max_cod": 20000000,
            "orphan_timeout": 900
        },
        "delivery_type": "SAMEDAY",
        "notify_package_return": True,
        "parent_id": "",
        "uniform_verify": False,
        "payment_method": [
            {
                "description": "Cash",
                "description_vi_vn": "Tiền mặt",
                "payment": "cash",
                "order": 1
            },
            {
                "description": "Balance",
                "description_vi_vn": "Ví AhaMove",
                "payment": "balance",
                "order": 2
            },
            {
                "description": "MoMo e-Wallet",
                "description_vi_vn": "Ví điện tử MoMo",
                "payment": "momo",
                "order": 3
            },
            {
                "description": "ZaloPay e-Wallet",
                "description_vi_vn": "Ví điện tử ZaloPay",
                "payment": "Zalopay",
                "order": 4
            }
        ],
        "partner": True,
        "same_district_delivery": False,
        "same_district_delivery_areas": [
            "VN.HC.BC",
            "VN.HC.BH",
            "VN.HC.BT",
            "VN.HC.CG",
            "VN.HC.CC",
            "VN.HC.GV",
            "VN.HC.HM",
            "VN.HC.NB",
            "VN.HC.PN",
            "VN.HC.QA",
            "VN.HC.QJ",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.QB",
            "VN.HC.QC",
            "VN.HC.QD",
            "VN.HC.QE",
            "VN.HC.QF",
            "VN.HC.QG",
            "VN.HC.QH",
            "VN.HC.QI",
            "VN.HC.TD",
            "VN.HC.TB",
            "VN.HC.TP"
        ],
        "vat_rate": 0.1,
        "pod_type": "photo",
        "require_pod": True,
        "enable_cancellation_punishment": True,
        "is_child_service": True,
        "opening_hours": "10-13",
        "animated_url": "https://i.imgur.com/xiDxEYN.png",
        "requests": [
            {
                "_id": "SGN-2H-PUBLIC-THERMALBAG",
                "name": "Túi giữ nhiệt",
                "name_vi_vn": "Túi giữ nhiệt",
                "enable": True,
                "name_en_us": "Thermal Bag",
                "icon_url": "https://trello-attachments.s3.amazonaws.com/5eabe9291dc6933e9e74eb2f/5f8531508904fa20c3cc89ad/1545287f04ffcc958416ab13b8bc3de5/2710.png",
                "order": 1,
                "price": 0,
                "no_commission": False,
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-2H-PUBLIC",
                "supplier_description_vi_vn": "Đối tác được cộng thêm 5.000đ/đơn hàng có đặt dịch vụ Túi giữ nhiệt",
                "supplier_description": "Đối tác được cộng thêm 5.000đ/đơn hàng có đặt dịch vụ Túi giữ nhiệt",
                "supplier_description_url": "https://ahamove.com/tui-giu-nhiet-chuyen-nghiep-tung-giay/",
                "img_url": "",
                "description_vi_vn": "Đơn hàng sẽ được đảm bảo vận chuyển bằng túi giữ nhiệt của AhaMove, giúp khách hàng yên tâm về việc đảm bảo chất lượng hàng hóa 100% khi giao đến khách hàng. Phù hợp với sản phẩm là hàng tươi sống, đông lạnh, các mặt hàng đồ ăn thức uống cần đảm bảo nhiệt độ.",
                "description_en_us": "To make sure the quality of goods when delivered, each orders will be packed by AhaMove's thermal bags. Suitable for fresh, frozen food or beverages that need to be stored in Temperature-Controlled enviroment.",
                "path_index": 0
            }
        ],
        "currency": "VND"
    },
    {
        "_id": "SGN-TRUCK-500-AHAPRO",
        "enable": True,
        "order": 5,
        "city_id": "SGN",
        "name": "Xe tải 500kg",
        "rebroadcast_interval": 1200,
        "rebroadcast_limit": 3,
        "name_vi_vn": "Xe tải 500kg",
        "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/services/truck/Truck-500.png",
        "map_icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/services/Truck_service_map_icon/Truck.png",
        "parent_id": "SGN-TRUCK",
        "stop_fee": 11000,
        "commission_type": "PERCENTAGE",
        "commission_value": 0.212,
        "distance_fee": "185000 if x <= 4 else 185000 + (x - 4) * 22000 if x <= 10 else 185000 + 6 * 22000 + (x - 10) * 16000 if x <= 15 else 185000 + 6 * 22000 + 5 * 16000  + (x - 15) * 15500",
        "vat_rate": 0.1,
        "require_to": True,
        "broadcast_distance": 50000,
        "name_en_us": "Truck 500kg",
        "max_stop_points": 5,
        "max_cod": 10000000,
        "enable_platform": [
            "momo_deeplink",
            "momo_permission",
            "zalo",
            "zalopay",
            "smartpay_deeplink",
            "VIETTEL",
            "onwheel"
        ],
        "cross_service": {
            "enable": True,
            "services": [
                "SGN-TRUCK-2000"
            ]
        },
        "max_concurrent_orders": 5,
        "is_recommend": False,
        "delivery_type": "TRUCK",
        "notify_package_return": True,
        "description_en_us": "📦 (LxWxH) 1.4 x 1.4 x 1 meters",
        "description_vi_vn": "📦 (DxRxC) 1.4 x 1.4 x 1 mét",
        "fee_description_vi_vn": "Khối lượng chuyên chở: 500kg\nHàng hoá phù hợp (DxRxC): 1.4 x 1.4 x 1 mét\n\nPhí quãng đường:\n- Từ 00 - 04km: 185,000đ\n- Từ 04 - 10km: 20,000đ/km\n- Từ 10 - 15km: 14,375đ/km\n- Trên 15km: 14,000đ/km\n\nKhung giờ cấm tải (Nội thành)\n- Từ 06:00 - 09:00 AM\n- Từ 16:00 - 20:00 PM\n*Mách bạn: Hãy sử dụng xe tải VAN trong khung giờ cấm tải để tối ưu đơn hàng\n\nMức COD tối đa: 10,000,000đ\nPhí COD:\n- COD <   2,000,000đ: Miễn phí\n- COD >= 2,000,000đ: 0.8% x Giá trị COD",
        "fee_description_en_us": "Payload capacity: 500kg\nSuitable goods (LxWxH): 1.4 x 1.4 x 1 meters\n\nDistance fee:\n- From 00 - 04km: 185,000 VND\n- From 04 - 10km: 20,000 VND/km\n- From 10 - 15km: 14,375 VND/km\n- Over 15km: 14,000 VND/km\n\nTruck ban hours (Urban areas)\n- From 06:00 - 09:00 AM\n- From 16:00 - 20:00 PM\n*Tip: Use VAN during truck ban hours to optimize orders\n\nMaximum COD: 10,000,000 VND\nCOD fee:\n- COD <   2,000,000 VND: Free\n- COD >= 2,000,000 VND: 0.8% x Value of COD",
        "group_name_en_us": "Large parcel delivery",
        "group_name_vi_vn": "Hàng hóa kích thước lớn",
        "auto_assign": True,
        "recommendation_config": {
            "supplier_timeout": 30,
            "recommend_timeout": 90,
            "recommend_radius": 3500,
            "sleep_interval": 90,
            "dispatch_mode": "RECOMMEND",
            "pool_mode": "NO_POOL",
            "pool_saving_threshold": 0.2,
            "poolable": False
        },
        "vehicle_info": {
            "image": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/services/truck/Truck-500.png",
            "length": 1.4,
            "width": 1.4,
            "height": 1.2,
            "weight": 500.0,
            "box_volume": 10,
            "short_intro_vi": "Thích hợp cho hàng hoá nhỏ và không hoạt động trong khung giờ cấm tải ",
            "short_intro_en": "This vehicle is suitable to carry small parcels and deactive in truck ban hours",
            "short_description_vi": "1.4 x 1.4 x 1.0 mét. Lên tới 500kg",
            "short_description_en": "1.4 x 2.4 x 1.0 Meter. Up to 500kgs"
        },
        "distance_fee_v3": {
            "blocks": [
                {
                    "from": 0,
                    "to": 4,
                    "base": 185000,
                    "price_multiplier": 0
                },
                {
                    "from": 4,
                    "to": 10,
                    "base": 185000,
                    "price_multiplier": 22000
                },
                {
                    "from": 10,
                    "to": 15,
                    "base": 317000,
                    "price_multiplier": 16000
                },
                {
                    "from": 15,
                    "to": 100000,
                    "base": 397000,
                    "price_multiplier": 15500
                }
            ],
            "hour_rates": []
        },
        "timeout": 120001,
        "available_districts": [
            "VN.HC.BC",
            "VN.HC.NB",
            "VN.TP",
            "VN.HC.BH",
            "VN.HC.BT",
            "VN.HC.GV",
            "VN.HC.PN",
            "VN.HC.QJ",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.QA",
            "VN.HC.QB",
            "VN.HC.QC",
            "VN.HC.QD",
            "VN.HC.QE",
            "VN.HC.QF",
            "VN.HC.QG",
            "VN.HC.QH",
            "VN.HC.QI",
            "VN.HC.TB",
            "VN.HC.TD"
        ],
        "drop_off_districts": [
            "VN.HC.BC",
            "VN.HC.CC",
            "VN.HC.CG",
            "VN.HC.HM",
            "VN.HC.NB",
            "VN.TDM",
            "VN.CM",
            "VN.BH",
            "VN.BB",
            "VN.LT",
            "VN.TA",
            "VN.XL",
            "VN.VC",
            "VN.BC",
            "VN.LK",
            "VN.TP",
            "VN.PG",
            "VN.VT.VT",
            "VN.VT.BR",
            "VN.VT.CD",
            "VN.VT.XM",
            "VN.VT.TT",
            "VN.VT.LD",
            "VN.VT.DD",
            "VN.VT.CD",
            "VN.DA",
            "VN.HC.BH",
            "VN.HC.BT",
            "VN.HC.GV",
            "VN.HC.PN",
            "VN.HC.QJ",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.QA",
            "VN.HC.QB",
            "VN.HC.QC",
            "VN.HC.QD",
            "VN.HC.QE",
            "VN.HC.QF",
            "VN.HC.QG",
            "VN.HC.QH",
            "VN.HC.QI",
            "VN.HC.TB",
            "VN.HC.TP",
            "VN.HC.TD"
        ],
        "opening_hours": "0-23",
        "enable_cancellation_punishment": False,
        "truck_ban": {
            "ban_districts": [
                {
                    "_id": 266,
                    "hasc_2": "VN.HC.NB",
                    "name_2": "Nhà Bè",
                    "city_id": "SGN",
                    "name": "NB",
                    "tick": True,
                    "spc_sKXFW": 0,
                    "idx_sKXFW": 1
                }
            ],
            "ban_hours": [
                {
                    "from": 15,
                    "to": 20
                }
            ],
            "recommend_service": "SGN-VAN-500",
            "enable": False
        },
        "map_icon_3d": {
            "url": "https://firebasestorage.googleapis.com/v0/b/aha-chat-292008.appspot.com/o/3dicon%2Ftruck-500.png?alt=media&token=c11b2e4e-1dfb-46aa-9d76-8574e234a001",
            "sprite_size": 64,
            "sprite_count": 64
        },
        "priority_score": 6,
        "assigning_before": [
            {
                "from": 0,
                "to": 7,
                "value": 10800
            },
            {
                "from": 16,
                "value": 3600,
                "to": 18
            },
            {
                "from": 18,
                "to": 20,
                "value": 400
            },
            {
                "from": 20,
                "to": 23,
                "value": 1000
            }
        ],
        "max_item_value": 30000000.0,
        "animated_url": "https://i.imgur.com/xiDxEYN.png",
        "requests": [
            {
                "_id": "SGN-TRUCK-500-AHAPRO-INSURANCE",
                "name": "Khai giá hàng hoá",
                "name_vi_vn": "Khai giá hàng hoá",
                "name_en_us": "Value declaration",
                "enable": True,
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/Insurance/secure+24x24%402x.png",
                "order": 1,
                "price_blocks": [
                    {
                        "from": 0,
                        "to": 10000001,
                        "price": 5000,
                        "description_vi_vn": "Bồi thường mất mát hoặc hư hỏng theo giá trị hàng hoá của bạn",
                        "description_en_us": "Coverage for loss or damage according to the value of your items"
                    },
                    {
                        "from": 10000001,
                        "to": 20000001,
                        "price": 10000,
                        "description_vi_vn": "Bồi thường mất mát hoặc hư hỏng theo giá trị hàng hoá của bạn",
                        "description_en_us": "Coverage for loss or damage according to the value of your items"
                    },
                    {
                        "from": 20000001,
                        "to": 1000000000,
                        "price": 15000,
                        "description_vi_vn": "Bồi thường mất mát hoặc hư hỏng theo giá trị hàng hoá của bạn",
                        "description_en_us": "Coverage for loss or damage according to the value of your items"
                    }
                ],
                "no_supplier_payout": True,
                "type": "COD_INSURANCE",
                "applied_stp_num": 5,
                "service_id": "SGN-TRUCK-500-AHAPRO",
                "description_url": "https://www.ahamove.com/aha-pro-cod-va-khai-gia/",
                "benefit_url": "https://www.ahamove.com/aha-pro-cod-va-khai-gia/",
                "non_cod_description": "Bồi thường mất mát hoặc hư hỏng theo danh mục hàng hoá của bạn",
                "none_cod_price_blocks": {
                    "electronics": 1000,
                    "health & beauty": 1000,
                    "housing & lifestyle": 1000,
                    "food": 1000,
                    "mother & baby": 1000,
                    "fashion": 1000,
                    "grocery": 1000,
                    "restaurant": 1000,
                    "sport": 1000,
                    "drink": 1000,
                    "other": 400,
                    "individual needs": 1000,
                    "transportation": 1000
                },
                "required_item_value": False,
                "max_item_value": 10000000
            }
        ],
        "currency": "VND"
    },
    {
        "_id": "SGN-4H",
        "enable": True,
        "order": 6,
        "city_id": "SGN",
        "name": "Pooling",
        "broadcast_distance": 3500,
        "name_vi_vn": "Pooling",
        "icon_url": "http://sw001.hstatic.net/9/12db9172e9ec55/pooling_3_resized.png",
        "map_icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/tv_motorcycle.png",
        "parent_id": "",
        "distance_fee": "24000 if x <= 6 else 24000 + (x - 6) * 4000",
        "commission_type": "PERCENTAGE",
        "commission_value": 0.3,
        "stop_fee": 5000,
        "name_en_us": "Pooling",
        "require_to": True,
        "name_vi_VN": "Pooling",
        "auto_assign": False,
        "auto_assign_distance": 3000,
        "require_request": False,
        "advance_broadcast_distance": 0,
        "timeout": 300,
        "cod": 10000000,
        "auto_assign_districts": [
            "VN.HC.QA",
            "VN.HC.QC",
            "VN.HC.QD",
            "VN.HC.QE",
            "VN.HC.QJ",
            "VN.HC.QK",
            "VN.HC.TB",
            "VN.HC.PN",
            "VN.HC.BH",
            "VN.HC.TP"
        ],
        "first_order_cod": 700000,
        "transfer_cod": True,
        "pool": True,
        "pool_timeout_commission_value": 0.1,
        "accept_interval": 0,
        "max_stop_points": 1,
        "rebroadcast_interval": 10,
        "cross_service": {
            "enable": False,
            "services": []
        },
        "recommendation_config": {
            "supplier_timeout": 20,
            "recommend_timeout": 100,
            "poolable": True
        },
        "require_pop": True,
        "priority_score": 6,
        "distance_fee_v3": {
            "blocks": [
                {
                    "from": 0,
                    "to": 6,
                    "base": 24000,
                    "price_multiplier": 0
                },
                {
                    "from": 6,
                    "to": 100000,
                    "base": 24000,
                    "price_multiplier": 4000
                }
            ],
            "hour_rates": []
        },
        "animated_url": "https://i.imgur.com/xiDxEYN.png",
        "requests": [],
        "currency": "VND"
    },
    {
        "_id": "SGN-TRICYCLE",
        "enable": True,
        "order": 7,
        "city_id": "SGN",
        "name": "Xe Ba Gác",
        "rebroadcast_interval": 1200,
        "rebroadcast_limit": 3,
        "name_vi_vn": "Xe Ba Gác",
        "name_en_us": "Tricycle",
        "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/services/truck/tricycle.png",
        "map_icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/services/Truck_service_map_icon/Tricycle.png",
        "parent_id": "",
        "stop_fee": 11000,
        "commission_type": "PERCENTAGE",
        "commission_value": 0.212,
        "distance_fee": "165000 if x <= 4 else 165000 + (x - 4) * 20000 if x <= 10 else 165000 + 6 * 20000 + (x - 10) * 15000 if x <= 15 else 165000 + 6 * 20000 + 5 * 15000  + (x - 15) * 14500",
        "vat_rate": 0.1,
        "broadcast_distance": 3000,
        "accept_interval": 1800,
        "require_to": True,
        "max_stop_points": 10,
        "notify_package_return": True,
        "vehicle_info": {
            "image": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/services/truck/tricycle.png",
            "length": 1.8,
            "width": 1.2,
            "height": 0.8,
            "box_volume": 10,
            "weight": 500.0,
            "short_intro_vi": "Thích hợp cho hàng hoá nhỏ và di chuyển trong hẻm khu vực nội thành ",
            "short_intro_en": "This vehicle is suitable to carry small parcels and to move alley and intra city ",
            "short_description_vi": "1.8 x 1.2 x 0.8 mét. Lên tới 400kg",
            "short_description_en": "1.8 x 1.2 x 0.8 meter. Up to 400kgs",
            "description_vi_vn": "\"Khối lượng chuyên chở: 400kg\nHàng hoá phù hợp (DxRxC): 1.8 x 1.2 x 0.8 mét\n\nPhí quãng đường:\n- Từ 00 - 04km: 165,000đ\n- Từ 04 - 10km: 20,000đ/km\n- Từ 10 - 15km: 15,000đ/km\n- Trên 15km: 14,500đ/km\n\nPhí điểm dừng: 11,000đ/điểm dừng\n\nKhung giờ cấm tải (Nội thành)\n- Từ 06:00 - 09:00 AM\n- Từ 16:00 - 19:00 PM (HN) / 20:00 PM (TP.HCM)\n*Lưu ý: Xe ba gác chỉ hoạt động trong khu vực nội thành\n*Mách bạn: Hãy sử dụng xe tải VAN trong khung giờ cấm tải để tối ưu đơn hàng\n\nMức COD tối đa: 10,000,000đ\nPhí COD:\n- COD <   2,000,000đ: Miễn phí\n- COD >= 2,000,000đ: 0.88% x Giá trị COD\"",
            "description_en_us": "\"Payload capacity: 400kg\nSuitable goods (LxWxH): 1.8 x 1.2 x 0.8 meters\n\nDistance fee:\n- From 00 - 04km: 165,000 VND\n- From 04 - 10km: 20,000 VND/km\n- From 10 - 15km: 15,000 VND/km\n- Over 15km: 14,500 VND/km\n\nStop-fee: 11,000 VND/stop\n\nTruck ban hours (Urban areas)\n- From 06:00 - 09:00 AM\n- From 16:00 - 19:00 PM (HN) / 20:00 PM (TP.HCM)\n*Note: Tricycle operates in urban areas only \n*Tip: Use VAN during truck ban hours to optimize orders\n\nMaximum COD: 10,000,000 VND\nCOD fee:\n- COD <   2,000,000 VND: Free\n- COD >= 2,000,000 VND: 0.88% x Value of COD\""
        },
        "description_en_us": "📦 (LxWxH) 1.8 x 1.2 x 0.8 meters",
        "description_vi_vn": "📦 (DxRxC) 1.8 x 1.2 x 0.8 mét",
        "fee_description_en_us": "Payload capacity: 400kg\nSuitable goods (LxWxH): 1.8 x 1.2 x 0.8 meters\n\nDistance fee:\n- From 00 - 04km: 165,000 VND\n- From 04 - 10km: 18,000 VND/km\n- From 10 - 15km: 13,750 VND/km\n- Over 15km: 13,000 VND/km\n\nTruck ban hours (Urban areas)\n- From 06:00 - 09:00 AM\n- From 16:00 - 20:00 PM\n*Note: Tricycle operates in urban areas only \n*Tip: Use VAN during truck ban hours to optimize orders\n\nMaximum COD: 10,000,000 VND\nCOD fee:\n- COD <   2,000,000 VND: Free\n- COD >= 2,000,000 VND: 0.8% x Value of COD",
        "fee_description_vi_vn": "Khối lượng chuyên chở: 400kg\nHàng hoá phù hợp (DxRxC): 1.8 x 1.2 x 0.8 mét\n\nPhí quãng đường:\n- Từ 00 - 04km: 165,000đ\n- Từ 04 - 10km: 18,000đ/km\n- Từ 10 - 15km: 13,750đ/km\n- Trên 15km: 13,000đ/km\n\nKhung giờ cấm tải (Nội thành)\n- Từ 06:00 - 09:00 AM\n- Từ 16:00 - 20:00 PM\n*Lưu ý: Xe ba gác chỉ hoạt động trong khu vực nội thành\n *Mách bạn: Hãy sử dụng xe tải VAN trong khung giờ cấm tải để tối ưu đơn hàng \n \nMức COD tối đa: 10,000,000đ\nPhí COD:\n- COD <   2,000,000đ: Miễn phí\n- COD >= 2,000,000đ: 0.8% x Giá trị COD",
        "cross_service": {
            "enable": True,
            "services": [
                "SGN-TRICYCLE",
                "SGN-TRUCK-1000",
                "SGN-TRUCK-500",
                "SGN-VAN-500",
                "SGN-VAN-1000"
            ]
        },
        "cross_city": {
            "enable": True,
            "cities": [
                "SGN",
                "THD",
                "BHC"
            ]
        },
        "timeout": 1800,
        "cod": 10000000,
        "max_cod": 10000000,
        "delivery_type": "TRUCK",
        "available_districts": [
            "VN.HC.CC",
            "VN.HC.NB",
            "VN.HC.QK",
            "VN.HC.QE",
            "VN.HC.BH",
            "VN.HC.TD",
            "VN.HC.HM",
            "VN.HC.GV",
            "VN.HC.QC",
            "VN.HC.QA",
            "VN.HC.TD",
            "VN.HC.TP",
            "VN.HC.QD",
            "VN.HC.BT",
            "VN.HC.CG",
            "VN.HC.QG",
            "VN.HC.TD",
            "VN.HC.TB",
            "VN.HC.QF",
            "VN.HC.QH",
            "VN.HC.PN",
            "VN.HC.QJ",
            "VN.HC.BC",
            "VN.HC.QL"
        ],
        "cod_commission": {
            "value": 0.008,
            "none_commission_limit": 2000000
        },
        "advance_broadcast_distance": 14500,
        "payment_method": [
            {
                "description": "Cash",
                "description_vi_vn": "Tiền mặt",
                "payment": "cash",
                "order": 1
            },
            {
                "description": "Balance",
                "description_vi_vn": "Ví AhaMove",
                "payment": "balance",
                "order": 2
            },
            {
                "description": "MoMo e-Wallet",
                "description_vi_vn": "Ví điện tử MoMo",
                "payment": "momo",
                "order": 3
            },
            {
                "description": "ZaloPay e-Wallet",
                "description_vi_vn": "Ví điện tử ZaloPay",
                "payment": "Zalopay",
                "order": 4
            }
        ],
        "recommendation_config": {
            "supplier_timeout": 30,
            "recommend_timeout": 90,
            "recommend_radius": 2000,
            "sleep_interval": 90,
            "dispatch_mode": "RECOMMEND",
            "pool_mode": "NO_POOL",
            "pool_saving_threshold": 0.2,
            "poolable": False
        },
        "enable_platform": [
            "momo_deeplink",
            "momo_permission",
            "zalo",
            "zalopay",
            "smartpay_deeplink",
            "viettel-pay_deeplink",
            "onwheel"
        ],
        "drop_off_districts": [
            "VN.HC.CC",
            "VN.HC.NB",
            "VN.HC.QK",
            "VN.HC.QE",
            "VN.HC.BH",
            "VN.HC.TD",
            "VN.HC.HM",
            "VN.HC.GV",
            "VN.HC.QC",
            "VN.HC.QA",
            "VN.HC.TD",
            "VN.HC.TP",
            "VN.HC.QD",
            "VN.HC.BT",
            "VN.HC.CG",
            "VN.HC.QG",
            "VN.HC.TD",
            "VN.HC.TB",
            "VN.HC.QF",
            "VN.HC.QH",
            "VN.HC.PN",
            "VN.HC.QJ",
            "VN.HC.BC",
            "VN.HC.QL"
        ],
        "advance_max_concurrent_orders": 1,
        "max_concurrent_orders": 2,
        "same_district_delivery": False,
        "same_district_delivery_areas": [
            "VN.HC.BC",
            "VN.HC.BH",
            "VN.HC.BT",
            "VN.HC.CG",
            "VN.HC.CC",
            "VN.HC.GV",
            "VN.HC.HM",
            "VN.HC.NB",
            "VN.HC.PN",
            "VN.HC.QA",
            "VN.HC.QJ",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.QB",
            "VN.HC.QC",
            "VN.HC.QD",
            "VN.HC.QE",
            "VN.HC.QF",
            "VN.HC.QG",
            "VN.HC.QH",
            "VN.HC.QI",
            "VN.HC.TD",
            "VN.HC.TB",
            "VN.HC.TP"
        ],
        "group_name_en_us": "Tải trọng nhỏ",
        "group_name_vi_vn": "Tải trọng nhỏ",
        "supplier_description": "Thực hiện dưới 90 phút, nhận tối đa 1 đơn",
        "supplier_description_url": "https://ahamove.com/dich-vu-ba-gac-tai-tai-van/",
        "enable_cancellation_punishment": False,
        "distance_fee_v3": {
            "blocks": [
                {
                    "from": 0,
                    "to": 4,
                    "base": 165000,
                    "price_multiplier": 0
                },
                {
                    "from": 4,
                    "to": 10,
                    "base": 165000,
                    "price_multiplier": 20000
                },
                {
                    "from": 10,
                    "to": 15,
                    "base": 285000,
                    "price_multiplier": 15000
                },
                {
                    "from": 15,
                    "to": 100000,
                    "base": 360000,
                    "price_multiplier": 14500
                }
            ],
            "hour_rates": []
        },
        "map_icon_3d": {
            "url": "https://firebasestorage.googleapis.com/v0/b/aha-chat-292008.appspot.com/o/3dicon%2Fsgn-bike-v1.png?alt=media&token=6183f369-1ffb-4286-a947-e95ef996e00a",
            "sprite_size": 64,
            "sprite_count": 64
        },
        "priority_score": 6,
        "pending_period": 86400,
        "assigning_before": [
            {
                "from": 0,
                "to": 7,
                "value": 10800
            },
            {
                "from": 7,
                "to": 12,
                "value": 900
            },
            {
                "from": 12,
                "to": 16,
                "value": 1800
            }
        ],
        "is_tip_allowed": True,
        "default_vehicles": [
            "TRICYCLE"
        ],
        "is_select_vehicle_allowed": True,
        "alternative_vehicles": [
            "VAN-500",
            "TRUCK-500",
            "TRUCK-1000"
        ],
        "group_id": "TRICYCLE",
        "animated_url": "https://i.imgur.com/xiDxEYN.png",
        "requests": [
            {
                "_id": "SGN-TRICYCLE-CHUYENNHA",
                "name": "Gói hỗ trợ chuyển nhà cơ bản (Gồm hỗ trợ bốc xếp 1 tầng lầu 2 chiều và phí chờ 1 giờ)",
                "name_vi_vn": "Gói hỗ trợ chuyển nhà cơ bản (Gồm hỗ trợ bốc xếp 1 tầng lầu 2 chiều và phí chờ 1 giờ)",
                "name_en_us": "Gói hỗ trợ chuyển nhà cơ bản (Gồm hỗ trợ bốc xếp 1 tầng lầu 2 chiều và phí chờ 1 giờ)",
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/house-moving_s.png",
                "order": 1,
                "price": 300000,
                "description_vi_vn": "Chi tiết gói: \n- Hỗ trợ bốc xếp: 240000\n- Phí chờ: 60000\n \n Lưu ý: \n- Địa hình vận chuyển: Không quá 100m và 2 tầng/ lầu tại 2 chiều.\n- Vui lòng tháo lắp đồ điện lạnh, nội thất và đóng gói hàng hoá trước khi đặt dịch vụ\n- Trường hợp có phát sinh cước luân chuyển, bốc xếp vui lòng liên hệ tổng đài 1900545411 để được xác nhận.",
                "description_en_us": "Chi tiết gói: \n- Hỗ trợ bốc xếp: 240000\n- Phí chờ: 60000\n \n Lưu ý: \n- Địa hình vận chuyển: Không quá 100m và 2 tầng/ lầu tại 2 chiều.\n- Vui lòng tháo lắp đồ điện lạnh, nội thất và đóng gói hàng hoá trước khi đặt dịch vụ\n- Trường hợp có phát sinh cước luân chuyển, bốc xếp vui lòng liên hệ tổng đài 1900545411 để được xác nhận.",
                "type": "BOOLEAN",
                "description": "Chi tiết gói: \n- Hỗ trợ bốc xếp: 240000\n- Phí chờ: 60000\n \n Lưu ý: \n- Địa hình vận chuyển: Không quá 100m và 2 tầng/ lầu tại 2 chiều.\n- Vui lòng tháo lắp đồ điện lạnh, nội thất và đóng gói hàng hoá trước khi đặt dịch vụ\n- Trường hợp có phát sinh cước luân chuyển, bốc xếp vui lòng liên hệ tổng đài 1900545411 để được xác nhận.",
                "service_id": "SGN-TRICYCLE",
                "img_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/house-moving_s.png",
                "enable": True,
                "options": [
                    {
                        "code": "ITEM_1",
                        "name_vi_vn": "Hỗ trợ bốc xếp",
                        "name_en_us": "Hỗ trợ bốc xếp",
                        "selectable": True
                    },
                    {
                        "code": "ITEM_2",
                        "name_vi_vn": "Phí chờ",
                        "name_en_us": "Phí chờ",
                        "selectable": True
                    },
                    {
                        "code": "ITEM_3",
                        "name_vi_vn": "Combo Bốc xếp và phí chờ",
                        "name_en_us": "Combo Bốc xếp và phí chờ",
                        "selectable": True
                    }
                ],
                "service_group_id": "TRICYCLE",
                "group_id": "CHUYENNHA"
            },
            {
                "_id": "SGN-TRICYCLE-INSURANCE",
                "name": "Khai giá hàng hoá",
                "name_vi_vn": "Khai giá hàng hoá",
                "name_en_us": "Value declaration",
                "enable": True,
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/Insurance/secure+24x24%402x.png",
                "order": 1,
                "price_blocks": [
                    {
                        "from": 0,
                        "to": 10000000,
                        "price": 2000,
                        "description_vi_vn": "Bồi thường mất mát hoặc hư hỏng theo giá trị hàng hoá của bạn",
                        "description_en_us": "Coverage for loss or damage according to the value of your items"
                    }
                ],
                "no_supplier_payout": True,
                "type": "COD_INSURANCE",
                "applied_stp_num": 10,
                "required_item_value": True,
                "service_id": "SGN-TRICYCLE",
                "description_url": "https://ahamove.com/phi-khai-gia-cho-truck-ahmxsaladin/",
                "benefit_url": "https://ahamove.com/phi-khai-gia-cho-truck-ahmxsaladin/",
                "non_cod_description": "Bồi thường mất mát hoặc hư hỏng theo danh mục hàng hoá của bạn",
                "none_cod_price_blocks": {
                    "electronics": 2000,
                    "health & beauty": 2000,
                    "housing & lifestyle": 2000,
                    "food": 2000,
                    "mother & baby": 2000,
                    "fashion": 2000,
                    "grocery": 2000,
                    "restaurant": 2000,
                    "sport": 2000,
                    "drink": 2000,
                    "other": 2000,
                    "individual needs": 2000,
                    "transportation": 2000
                },
                "service_group_id": "TRICYCLE"
            },
            {
                "_id": "SGN-TRICYCLE-LOADING",
                "name": "Bốc xếp hàng tầng lầu",
                "enable": True,
                "support_remarks": True,
                "name_vi_vn": "Bốc xếp hàng tầng lầu",
                "name_en_us": "Loading or Unloading",
                "icon_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/Special+Request/Special+Request+Icon/Bulky_packages.jpg",
                "order": 1,
                "tier_list": [
                    {
                        "code": "TIER_1",
                        "name_vi_vn": "Tiêu chuẩn",
                        "name_en_us": "Standard",
                        "selectable": False,
                        "price": 0,
                        "price_description_vi_vn": "Miễn phí",
                        "price_description_en_us": "Free",
                        "description_vi_vn": "50x40x50:30kg",
                        "description_en_us": "50x40x50:30kg",
                        "img_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/Special+Request/Bulky+Packages/Standard.png"
                    },
                    {
                        "code": "TIER_2",
                        "name_vi_vn": "Mức 1",
                        "name_en_us": "Package 1",
                        "price": 10000,
                        "selectable": True,
                        "description_vi_vn": "60x50x60:40kg",
                        "description_en_us": "60x50x60:40kg",
                        "img_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/Special+Request/Bulky+Packages/Tier+1.png"
                    },
                    {
                        "code": "TIER_3",
                        "name_vi_vn": "Mức 2",
                        "name_en_us": "Package 2",
                        "selectable": True,
                        "price": 20000,
                        "description_vi_vn": "70x60x70:60kg",
                        "description_en_us": "70x60x70:60kg",
                        "img_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/Special+Request/Bulky+Packages/Tier+2.png"
                    },
                    {
                        "code": "TIER_4",
                        "name_vi_vn": "Mức 3",
                        "name_en_us": "Package 3",
                        "selectable": True,
                        "price": 40000,
                        "description_vi_vn": "90x70x90:80kg",
                        "description_en_us": "90x70x90:80kg",
                        "img_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/Special+Request/Bulky+Packages/Tier+3.png"
                    },
                    {
                        "code": "TIER_MAX",
                        "name_vi_vn": "Quá tải trọng",
                        "name_en_us": "Over",
                        "selectable": False,
                        "price": -1,
                        "price_description_vi_vn": "Quá tải trọng",
                        "price_description_en_us": "Overload",
                        "description_vi_vn": "90x60x90cm (100kg)",
                        "description_en_us": "90x60x90cm (100kg)",
                        "warning_message": "Hàng hoá có kích thước lớn vượt quá quy định, không cho phép vận chuyển bằng xe máy",
                        "img_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/Special+Request/Bulky+Packages/Tier+max.png"
                    }
                ],
                "type": "TIER",
                "service_id": "SGN-TRICYCLE",
                "img_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/Special+Request/Special+Request+Icon/Bulky_packages.jpg",
                "description_vi_vn": "Giao hàng tầng lầu",
                "supplier_description_url": "https://ahamove.com/giao-hang-cong-kenh",
                "service_group_id": "TRUCK",
                "group_id": "LOADING"
            },
            {
                "_id": "SGN-TRICYCLE-2",
                "icon_url": "http://hstatic.net/797/1000010797/10/2016/7-14/money.png",
                "name": "PER UNIT",
                "name_vi_vn": "PER UNIT",
                "name_en_us": "PER UNIT",
                "order": 2,
                "price": 0,
                "max_input": 10,
                "type": "PER_UNIT",
                "service_id": "SGN-TRICYCLE",
                "enable": True,
                "service_group_id": "TRICYCLE"
            },
            {
                "_id": "SGN-TRICYCLE-LOADERS",
                "name": "Thêm người bốc xếp",
                "enable": True,
                "name_vi_vn": "Thêm người bốc xếp",
                "name_en_us": "Thêm người bốc xếp",
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/more-pickers.png",
                "img_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/more-pickers.png",
                "order": 2,
                "price": 300000,
                "max_input": 3,
                "description_vi_vn": "Hàng hoá số lượng lớn hay có kích thước cồng kềnh, nặng và yêu cầu phải có 2 người bưng trở lên",
                "no_commission": False,
                "description_en_us": "Hàng hoá số lượng lớn hay có kích thước cồng kềnh, nặng và yêu cầu phải có 2 người bưng trở lên",
                "type": "PER_UNIT",
                "description": "Hàng hoá số lượng lớn hay có kích thước cồng kềnh, nặng và yêu cầu phải có 2 người bưng trở lên",
                "service_id": "SGN-TRICYCLE",
                "service_group_id": "TRICYCLE",
                "group_id": "LOADER"
            },
            {
                "_id": "SGN-TRICYCLE-FLOOR",
                "name": "Hỗ trợ bốc xếp lên lầu ( + lầu)",
                "enable": True,
                "name_vi_vn": "Hỗ trợ bốc xếp lên lầu ( + lầu)",
                "name_en_us": "Hỗ trợ bốc xếp lên lầu ( + lầu)",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/sr_tipping.png",
                "img_url": "http://file.hstatic.net/1000010797/file/tipping_final.jpg",
                "order": 2,
                "price": 50000,
                "no_commission": False,
                "no_promotion": True,
                "description_vi_vn": "Hãy chọn dịch vụ kèm theo này nếu bạn cần bốc xếp hàng từ 2 tầng lầu, nơi không có thang máy. Một lần chọn thêm tương ứng với 1 tầng/lầu. Ví dụ số lượng 3 tương ứng với 3 tầng/lầu",
                "description_en_us": "Please choose this additional service if you need to load and unload goods from 2 floors where no elevator. One additional selection corresponds to 1 floor/floor. For example the number of 3 corresponds to 3 floors/floor",
                "type": "PER_UNIT",
                "description": "",
                "service_id": "SGN-TRICYCLE",
                "device_types": [
                    "web",
                    "android",
                    "ios"
                ],
                "max_input": 5
            },
            {
                "_id": "SGN-TRICYCLE-3",
                "name": "PERCENTAGE",
                "enable": True,
                "name_vi_vn": "PERCENTAGE",
                "name_en_us": "PERCENTAGE",
                "icon_url": "http://hstatic.net/797/1000010797/10/2016/7-14/money.png",
                "order": 3,
                "type": "COMMISSION_PERCENTAGE",
                "price": 0,
                "service_id": "SGN-TRICYCLE",
                "service_group_id": "TRICYCLE"
            },
            {
                "_id": "SGN-TRICYCLE-4",
                "name": "PERCENTAGE ON DISTANCE",
                "enable": True,
                "name_vi_vn": "PERCENTAGE ON DISTANCE",
                "name_en_us": "PERCENTAGE ON DISTANCE",
                "icon_url": "http://hstatic.net/797/1000010797/10/2016/7-14/money.png",
                "order": 4,
                "type": "COMMISSION_DISTANCE_PERCENTAGE",
                "price": 0.8,
                "service_id": "SGN-TRICYCLE",
                "service_group_id": "TRICYCLE"
            },
            {
                "_id": "SGN-TRICYCLE-5",
                "name": "FLAT COMMISSION ON USER INPUT",
                "enable": True,
                "name_vi_vn": "FLAT COMMISSION ON USER INPUT",
                "name_en_us": "FLAT COMMISSION ON USER INPUT",
                "icon_url": "http://hstatic.net/797/1000010797/10/2016/7-14/money.png",
                "price": 0,
                "type": "COMMISSION_FLAT",
                "order": 5,
                "service_id": "SGN-TRICYCLE",
                "service_group_id": "TRICYCLE"
            },
            {
                "_id": "SGN-TRICYCLE-6",
                "name": "ITEM",
                "enable": True,
                "name_vi_vn": "ITEM",
                "name_en_us": "ITEM",
                "icon_url": "http://hstatic.net/797/1000010797/10/2016/7-14/money.png",
                "img_url": "",
                "order": 6,
                "price": 5000,
                "item_price": 10000,
                "max_input": 5,
                "type": "ITEM",
                "service_id": "SGN-TRICYCLE",
                "service_group_id": "TRICYCLE"
            }
        ],
        "currency": "VND"
    },
    {
        "_id": "SGN-PICKUP-TRUCK",
        "enable": True,
        "order": 7,
        "city_id": "SGN",
        "name": "Xe Bán Tải",
        "name_vi_vn": "Xe Bán Tải",
        "name_en_us": "Xe Bán Tải",
        "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/aha-service/bantai.png",
        "map_icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/services/Truck_service_map_icon/Truck.png",
        "parent_id": "",
        "stop_fee": 11000,
        "commission_type": "PERCENTAGE",
        "commission_value": 0.212,
        "distance_fee": "165000 if x <= 4 else 165000 + (x - 4) * 20000 if x <= 10 else 165000 + 6 * 20000 + (x - 10) * 15000 if x <= 15 else 165000 + 6 * 20000 + 5 * 15000  + (x - 15) * 14500",
        "broadcast_distance": 4000,
        "accept_interval": 1800,
        "require_to": True,
        "max_stop_points": 10,
        "notify_package_return": True,
        "description_en_us": "📦 (LxWxH) 1.4 x 1.4 x 0.8 meters",
        "description_vi_vn": "📦 (DxRxC) 1.4 x 1.4 x 0.8 mét",
        "fee_description_en_us": "\"Payload capacity: 400kg\nSuitable goods (LxWxH): 1.4 x 1.4 x 0.8 meters\n\nDistance fee:\n- From 00 - 04km: 165,000 VND\n- From 04 - 10km: 20,000 VND/km\n- From 10 - 15km: 15,000 VND/km\n- Over 15km: 14,500 VND/km\n\nStop-fee: 11,000 VND/stop\n\nTruck ban hours (Urban areas)\n- From 06:00 - 09:00 AM\n- From 16:00 - 19:00 PM (HN) / 20:00 PM (TP.HCM)\n*Tip: Use VAN/PICK-UP Truck during truck ban hours to optimize orders\n\nMaximum COD: 10,000,000 VND\nCOD fee:\n- COD <   2,000,000 VND: Free\n- COD >= 2,000,000 VND: 0.88% x Value of COD\"",
        "fee_description_vi_vn": "\"Khối lượng chuyên chở: 400kg\nHàng hoá phù hợp (DxRxC): 1.4 x 1.4 x 0.8 mét\n\nPhí quãng đường:\n- Từ 00 - 04km: 165,000đ\n- Từ 04 - 10km: 20,000đ/km\n- Từ 10 - 15km: 15,000đ/km\n- Trên 15km: 14,500đ/km\n\nPhí điểm dừng: 11,000đ/điểm dừng\n\nKhung giờ cấm tải (Nội thành)\n- Từ 06:00 - 09:00 AM\n- Từ 16:00 - 19:00 PM (HN) / 20:00 PM (TP.HCM)\n*Mách bạn: Hãy sử dụng xe tải VAN/xe bán tải trong khung giờ cấm tải để tối ưu đơn hàng\n\nMức COD tối đa: 10,000,000đ\nPhí COD:\n- COD <   2,000,000đ: Miễn phí\n- COD >= 2,000,000đ: 0.88% x Giá trị COD\"",
        "cross_service": {
            "enable": False,
            "services": []
        },
        "cross_city": {
            "enable": False,
            "cities": []
        },
        "timeout": 1800,
        "cod": 10000000,
        "max_cod": 10000000,
        "delivery_type": "TRUCK",
        "available_districts": [
            "VN.HC.NB",
            "VN.HC.CC",
            "VN.HC.BC",
            "VN.HC.HM",
            "VN.HC.QB",
            "VN.HC.QC",
            "VN.HC.QG",
            "VN.HC.BH",
            "VN.HC.GV",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.PN",
            "VN.HC.QJ",
            "VN.HC.QD",
            "VN.HC.BT",
            "VN.HC.QF",
            "VN.HC.QA",
            "VN.HC.QE",
            "VN.HC.TB",
            "VN.HC.TD",
            "VN.HC.QH",
            "VN.HC.TP"
        ],
        "cod_commission": {
            "value": 0.0088,
            "none_commission_limit": 2000000
        },
        "advance_broadcast_distance": 4500,
        "payment_method": [
            {
                "description": "Cash",
                "description_vi_vn": "Tiền mặt",
                "payment": "cash",
                "order": 1
            },
            {
                "description": "Balance",
                "description_vi_vn": "Ví AhaMove",
                "payment": "balance",
                "order": 2
            },
            {
                "description": "MoMo e-Wallet",
                "description_vi_vn": "Ví điện tử MoMo",
                "payment": "momo",
                "order": 3
            },
            {
                "description": "ZaloPay e-Wallet",
                "description_vi_vn": "Ví điện tử ZaloPay",
                "payment": "Zalopay",
                "order": 4
            }
        ],
        "recommendation_config": {
            "supplier_timeout": 30,
            "recommend_timeout": 90,
            "recommend_radius": 2500,
            "sleep_interval": 90,
            "dispatch_mode": "RECOMMEND",
            "pool_mode": "NO_POOL",
            "pool_saving_threshold": 0.2,
            "poolable": False
        },
        "enable_platform": [
            "momo_deeplink",
            "momo_permission",
            "zalo",
            "zalopay",
            "smartpay_deeplink",
            "viettel-pay_deeplink"
        ],
        "advance_max_concurrent_orders": 1,
        "max_concurrent_orders": 1,
        "same_district_delivery": False,
        "same_district_delivery_areas": "",
        "group_name_en_us": "Tải trọng nhỏ",
        "group_name_vi_vn": "Tải trọng nhỏ",
        "supplier_description": "Thực hiện dưới 90 phút, nhận tối đa 1 đơn",
        "supplier_description_url": "https://ahamove.com/dich-vu-ba-gac-tai-tai-van/",
        "enable_cancellation_punishment": True,
        "vat_rate": 0.1,
        "tooltips": {
            "ASSIGNING": {
                "message": [
                    "Đơn hàng của bạn đã được AhaMove xác nhận.",
                    "Hệ thống đang tìm kiếm đối tác giao hàng.",
                    "Vui lòng chờ trong vòng 10 - 20 phút."
                ],
                "message_vi_vn": [
                    "Đơn hàng của bạn đã được AhaMove xác nhận.",
                    "Hệ thống đang tìm kiếm đối tác giao hàng.",
                    "Vui lòng chờ trong vòng 10 - 20 phút."
                ]
            },
            "ACCEPTED": {
                "message": [
                    "Xin chúc mừng! Đã có tài xế nhận đơn hàng của bạn.",
                    "Tài xế sẽ đến điểm lấy hàng trong vòng 15 - 60 phút.",
                    "Hãy liên hệ tài xế nếu bạn có bất kỳ thay đổi nào."
                ],
                "message_vi_vn": [
                    "Xin chúc mừng! Đã có tài xế nhận đơn hàng của bạn.",
                    "Tài xế sẽ đến điểm lấy hàng trong vòng 15 - 60 phút.",
                    "Hãy liên hệ tài xế nếu bạn có bất kỳ thay đổi nào."
                ]
            }
        },
        "rebroadcast_interval": 1200,
        "rebroadcast_limit": 3,
        "truck_ban": {
            "ban_districts": [
                {
                    "_id": 275,
                    "hasc_2": "VN.HC.QE",
                    "name_2": "Quận 5",
                    "city_id": "SGN",
                    "name": "QE",
                    "tick": True
                },
                {
                    "_id": 282,
                    "hasc_2": "VN.HC.TD",
                    "name_2": "Thủ Đức",
                    "city_id": "SGN",
                    "name": "TD",
                    "tick": True
                },
                {
                    "_id": 261,
                    "hasc_2": "VN.HC.BT",
                    "name_2": "Bình Tân",
                    "city_id": "SGN",
                    "name": "BT",
                    "tick": True
                },
                {
                    "_id": 269,
                    "hasc_2": "VN.HC.QK",
                    "name_2": "Quận 11",
                    "city_id": "SGN",
                    "name": "QK",
                    "tick": True
                },
                {
                    "_id": 279,
                    "hasc_2": "VN.HC.TD",
                    "name_2": "Quận 9",
                    "city_id": "SGN",
                    "name": "QI",
                    "tick": True
                },
                {
                    "_id": 260,
                    "hasc_2": "VN.HC.BH",
                    "name_2": "Bình Thạnh",
                    "city_id": "SGN",
                    "name": "BH",
                    "tick": True
                },
                {
                    "_id": 277,
                    "hasc_2": "VN.HC.QG",
                    "name_2": "Quận 7",
                    "city_id": "SGN",
                    "name": "QG",
                    "tick": True
                },
                {
                    "_id": 272,
                    "hasc_2": "VN.HC.TD",
                    "name_2": "Quận 2",
                    "city_id": "SGN",
                    "name": "QB",
                    "tick": True
                },
                {
                    "_id": 281,
                    "hasc_2": "VN.HC.TP",
                    "name_2": "Tân Phú",
                    "city_id": "SGN",
                    "name": "TP",
                    "tick": True
                },
                {
                    "_id": 271,
                    "hasc_2": "VN.HC.QA",
                    "name_2": "Quận 1",
                    "city_id": "SGN",
                    "name": "QA",
                    "tick": True
                },
                {
                    "_id": 268,
                    "hasc_2": "VN.HC.QJ",
                    "name_2": "Quận 10",
                    "city_id": "SGN",
                    "name": "QJ",
                    "tick": True
                },
                {
                    "_id": 273,
                    "hasc_2": "VN.HC.QC",
                    "name_2": "Quận 3",
                    "city_id": "SGN",
                    "name": "QC",
                    "tick": True
                },
                {
                    "_id": 278,
                    "hasc_2": "VN.HC.QH",
                    "name_2": "Quận 8",
                    "city_id": "SGN",
                    "name": "QH",
                    "tick": True
                },
                {
                    "_id": 259,
                    "hasc_2": "VN.HC.BC",
                    "name_2": "Bình Chánh",
                    "city_id": "SGN",
                    "name": "BC",
                    "tick": True
                },
                {
                    "_id": 264,
                    "hasc_2": "VN.HC.GV",
                    "name_2": "Gò Vấp",
                    "city_id": "SGN",
                    "name": "GV",
                    "tick": True
                },
                {
                    "_id": 276,
                    "hasc_2": "VN.HC.QF",
                    "name_2": "Quận 6",
                    "city_id": "SGN",
                    "name": "QF",
                    "tick": True
                },
                {
                    "_id": 267,
                    "hasc_2": "VN.HC.PN",
                    "name_2": "Phú Nhuận",
                    "city_id": "SGN",
                    "name": "PN",
                    "tick": True
                },
                {
                    "_id": 274,
                    "hasc_2": "VN.HC.QD",
                    "name_2": "Quận 4",
                    "city_id": "SGN",
                    "name": "QD",
                    "tick": True
                },
                {
                    "_id": 280,
                    "hasc_2": "VN.HC.TB",
                    "name_2": "Tân Bình",
                    "city_id": "SGN",
                    "name": "TB",
                    "tick": True
                },
                {
                    "_id": 270,
                    "hasc_2": "VN.HC.QL",
                    "name_2": "Quận 12",
                    "city_id": "SGN",
                    "name": "QL",
                    "tick": True
                }
            ],
            "ban_hours": [],
            "enable": False,
            "recommend_service": "SGN-VAN-1000"
        },
        "route_api_url": "http://ops-osrm-car.ops-tech:8080/route/v1/driving/",
        "pending_period": 86400,
        "max_cod_per_stop_point": 10000000,
        "vehicle_info": {
            "image": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/services/truck/bantai.png",
            "length": 1.4,
            "width": 1.4,
            "height": 0.8,
            "box_volume": 10,
            "weight": 500,
            "short_intro_vi": "Thích hợp xuống hầm chung cư và có thể di chuyển trong khung giờ cấm tải",
            "short_intro_en": "This vehicle is suitable to move down the basement apartment and moving in truck ban hours",
            "short_description_vi": "1.4 x 1.4 x 0.8 mét. Lên tới 400kg",
            "short_description_en": "1.4 x 1.4 x 0.8 meter. Up to 400kgs"
        },
        "is_tip_allowed": True,
        "assigning_before": [
            {
                "from": 0,
                "to": 7,
                "value": 2700
            },
            {
                "from": 7,
                "to": 12,
                "value": 1800
            },
            {
                "from": 11,
                "to": 13,
                "value": 2700
            },
            {
                "from": 13,
                "to": 16,
                "value": 1800
            },
            {
                "from": 16,
                "to": 24,
                "value": 2700
            }
        ],
        "max_item_value": 10000000,
        "distance_fee_v3": {
            "blocks": [
                {
                    "from": 0,
                    "to": 4,
                    "base": 165000,
                    "price_multiplier": 0
                },
                {
                    "from": 4,
                    "to": 10,
                    "base": 165000,
                    "price_multiplier": 20000
                },
                {
                    "from": 10,
                    "to": 15,
                    "base": 285000,
                    "price_multiplier": 15000
                },
                {
                    "from": 15,
                    "to": 100000,
                    "base": 360000,
                    "price_multiplier": 14500
                }
            ],
            "hour_rates": [
                {
                    "from": 0,
                    "to": 15.5,
                    "rate": 1
                },
                {
                    "from": 15.5,
                    "to": 20,
                    "rate": 1.2
                }
            ]
        },
        "alternative_vehicles": [
            "TRUCK-500",
            "VAN-500"
        ],
        "default_vehicles": [
            "PICKUP-TRUCK"
        ],
        "is_select_vehicle_allowed": True,
        "group_id": "PICKUP TRUCK",
        "animated_url": "https://i.imgur.com/xiDxEYN.png",
        "requests": [
            {
                "_id": "SGN-PICKUP-TRUCK-BOCXEP-KLLMC",
                "name": "Bốc xếp không lên lầu - 1 chiều",
                "name_en_us": "1 Way moving help (ground floor only)",
                "name_vi_vn": "Bốc xếp không lên lầu - 1 chiều",
                "icon_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_loading_per_helper.png",
                "order": 1,
                "price": 55000,
                "description_vi_vn": "Tài xế hỗ trợ bốc xếp hàng hóa (đã được đóng thùng) xuống xe đến địa điểm chỉ định trong vòng 100m HOẶC ngược lại (Áp dụng cho 1 lượt và không lên lầu). Các trường hợp phát sinh thêm, vui lòng thoả thuận với tài xế.",
                "description_en_us": "Driver provides moving help (already packaged) from vehicle to designated location within 100m OR vice versa (Apply for 1 turn and ground floor only). For additional cases, please negotiate with the driver.",
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-PICKUP-TRUCK",
                "img_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_loading_per_helper.png",
                "enable": True,
                "category": "UNLOADING",
                "service_group_id": "PICKUP TRUCK",
                "group_id": "BOCXEP"
            },
            {
                "_id": "SGN-PICKUP-TRUCK-CHUYENNHA",
                "name": "Gói hỗ trợ chuyển nhà cơ bản",
                "name_vi_vn": "Gói hỗ trợ chuyển nhà cơ bản",
                "name_en_us": "Gói hỗ trợ chuyển nhà cơ bản",
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/house-moving.png",
                "order": 1,
                "price": 300000,
                "description_vi_vn": "Chi tiết gói: \n- Hỗ trợ bốc xếp: 240000\nPhí chờ: 60000\n \n Lưu ý: \n- Địa hình vận chuyển: Không quá 100m và 2 tầng/ lầu tại 2 chiều.\n- Vui lòng tháo lắp đồ điện lạnh, nội thất và đóng gói hàng hoá trước khi đặt dịch vụ\n- Trường hợp có phát sinh cước luân chuyển, bốc xếp vui lòng liên hệ tổng đài 1900545411 để được xác nhận.",
                "description_en_us": "Chi tiết gói: \n- Hỗ trợ bốc xếp: 240000\n- Phí chờ: 60000\n \n Lưu ý: \n- Địa hình vận chuyển: Không quá 100m và 2 tầng/ lầu tại 2 chiều.\n- Vui lòng tháo lắp đồ điện lạnh, nội thất và đóng gói hàng hoá trước khi đặt dịch vụ\n- Trường hợp có phát sinh cước luân chuyển, bốc xếp vui lòng liên hệ tổng đài 1900545411 để được xác nhận.",
                "type": "BOOLEAN",
                "description": "Chi tiết gói: \n- Hỗ trợ bốc xếp: 240000\n- Phí chờ: 60000\n \n Lưu ý: \n- Địa hình vận chuyển: Không quá 100m và 2 tầng/ lầu tại 2 chiều.\n- Vui lòng tháo lắp đồ điện lạnh, nội thất và đóng gói hàng hoá trước khi đặt dịch vụ\n- Trường hợp có phát sinh cước luân chuyển, bốc xếp vui lòng liên hệ tổng đài 1900545411 để được xác nhận.",
                "service_id": "SGN-PICKUP-TRUCK",
                "img_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/house-moving.png",
                "enable": True,
                "options": [
                    {
                        "code": "ITEM_1",
                        "name_vi_vn": "Hỗ trợ bốc xếp",
                        "name_en_us": "Hỗ trợ bốc xếp",
                        "selectable": True
                    },
                    {
                        "code": "ITEM_2",
                        "name_vi_vn": "Phí chờ",
                        "name_en_us": "Phí chờ",
                        "selectable": True
                    },
                    {
                        "code": "ITEM_3",
                        "name_vi_vn": "Combo Bốc xếp và phí chờ",
                        "name_en_us": "Combo Bốc xếp và phí chờ",
                        "selectable": True
                    }
                ],
                "service_group_id": "PICKUP TRUCK",
                "group_id": "CHUYENNHA"
            },
            {
                "_id": "SGN-PICKUP-TRUCK-INSURANCE",
                "name": "Khai giá hàng hoá",
                "name_vi_vn": "Khai giá hàng hoá",
                "name_en_us": "Value declaration",
                "enable": True,
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/Insurance/secure+24x24%402x.png",
                "order": 1,
                "price_blocks": [
                    {
                        "from": 0,
                        "to": 10000001,
                        "price": 2000,
                        "description_vi_vn": "Bồi thường mất mát hoặc hư hỏng theo giá trị hàng hoá của bạn",
                        "description_en_us": "Coverage for loss or damage according to the value of your items"
                    }
                ],
                "no_supplier_payout": True,
                "type": "COD_INSURANCE",
                "applied_stp_num": 10,
                "required_item_value": True,
                "service_id": "SGN-PICKUP-TRUCK",
                "description_url": "https://ahamove.com/phi-khai-gia-cho-truck-ahmxsaladin/",
                "benefit_url": "https://ahamove.com/phi-khai-gia-cho-truck-ahmxsaladin/",
                "non_cod_description": "Bồi thường mất mát hoặc hư hỏng theo danh mục hàng hoá của bạn",
                "none_cod_price_blocks": {
                    "electronics": 2000,
                    "health & beauty": 2000,
                    "housing & lifestyle": 2000,
                    "food": 2000,
                    "mother & baby": 2000,
                    "fashion": 2000,
                    "grocery": 2000,
                    "restaurant": 2000,
                    "sport": 2000,
                    "drink": 2000,
                    "other": 2000,
                    "individual needs": 2000,
                    "transportation": 2000
                },
                "service_group_id": "PICKUP-TRUCK"
            },
            {
                "_id": "SGN-PICKUP-TRUCK-BOCXEP-KLLHC",
                "name": "Bốc xếp không lên lầu - 2 chiều",
                "name_vi_vn": "Bốc xếp không lên lầu - 2 chiều",
                "name_en_us": "2 Ways moving help (ground floor only)",
                "icon_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_loading_per_helper.png",
                "order": 2,
                "price": 77000,
                "description_vi_vn": "Tài xế hỗ trợ bốc xếp hàng hóa (đã được đóng thùng) xuống xe đến địa điểm chỉ định trong vòng 100m VÀ ngược lại (Áp dụng cho 2 lượt và không lên lầu). Các trường hợp phát sinh thêm, vui lòng thoả thuận với tài xế.",
                "description_en_us": "Driver provides moving help (already packaged) from vehicle to designated location within 100m AND vice versa (Apply for 2 turns and ground floor only). For additional cases, please negotiate with the driver.",
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-PICKUP-TRUCK",
                "img_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_loading_per_helper.png",
                "enable": True,
                "category": "UNLOADING",
                "service_group_id": "PICKUP TRUCK",
                "group_id": "BOCXEP"
            },
            {
                "_id": "SGN-PICKUP-TRUCK-LOADERS",
                "name": "Thêm người bốc xếp",
                "enable": True,
                "name_vi_vn": "Thêm người bốc xếp",
                "name_en_us": "Thêm người bốc xếp",
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/more-pickers.png",
                "img_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/more-pickers.png",
                "order": 2,
                "price": 300000,
                "max_input": 3,
                "description_vi_vn": "Hàng hoá số lượng lớn hay có kích thước cồng kềnh, nặng và yêu cầu phải có 2 người bưng trở lên",
                "no_commission": False,
                "description_en_us": "Hàng hoá số lượng lớn hay có kích thước cồng kềnh, nặng và yêu cầu phải có 2 người bưng trở lên",
                "type": "PER_UNIT",
                "description": "Hàng hoá số lượng lớn hay có kích thước cồng kềnh, nặng và yêu cầu phải có 2 người bưng trở lên",
                "service_id": "SGN-PICKUP-TRUCK",
                "service_group_id": "PICKUP TRUCK",
                "group_id": "LOADER"
            },
            {
                "_id": "SGN-PICKUP-TRUCK-BOCXEP-LLMC",
                "name": "Bốc xếp tại nhà có lầu - 1 chiều",
                "name_vi_vn": "Bốc xếp tại nhà có lầu - 1 chiều",
                "name_en_us": "1 Way moving help (Maximum 1 Floor)",
                "icon_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_moving_help_upstair.png",
                "order": 3,
                "price": 110000,
                "description_vi_vn": "Tài xế hỗ trợ bốc xếp hàng hóa (đã được đóng thùng) xuống xe đến địa điểm chỉ định trong vòng 100m HOẶC ngược lại (Áp dụng cho 1 lượt, 1 lầu). Các trường hợp phát sinh thêm, vui lòng thoả thuận với tài xế.",
                "description_en_us": "Driver provides moving help (already packaged) from vehicle to designated location within 100m OR vice versa (Apply for 1 turn and maximum 1 floor). For additional cases, please negotiate with the driver.",
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-PICKUP-TRUCK",
                "img_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_moving_help_upstair.png",
                "enable": True,
                "category": "UNLOADING",
                "service_group_id": "PICKUP TRUCK",
                "group_id": "BOCXEP"
            },
            {
                "_id": "SGN-PICKUP-TRUCK-BOCXEP-LLHC",
                "name": "Bốc xếp tại nhà có lầu - 2 chiều",
                "enable": True,
                "name_vi_vn": "Bốc xếp tại nhà có lầu - 2 chiều",
                "name_en_us": "2 Ways moving help (Maximum 1 Floor)",
                "icon_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_moving_help_upstair.png",
                "img_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_moving_help_upstair.png",
                "order": 4,
                "price": 165000,
                "description_vi_vn": "Tài xế hỗ trợ bốc xếp hàng hóa (đã được đóng thùng) xuống xe đến địa điểm chỉ định trong vòng 100m VÀ ngược lại (Áp dụng cho 2 lượt, 1 lầu). Các trường hợp phát sinh thêm, vui lòng thoả thuận với tài xế.",
                "description_en_us": "Driver provides moving help (already packaged) from vehicle to designated location within 100m AND vice versa (Apply for 1 turn and maximum 1 floor). For additional cases, please negotiate with the driver.",
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-PICKUP-TRUCK",
                "category": "UNLOADING",
                "service_group_id": "PICKUP TRUCK",
                "group_id": "BOCXEP"
            },
            {
                "_id": "SGN-PICKUP-TRUCK-ROUND-TRIP",
                "name": "Quay lại điểm lấy hàng",
                "name_vi_vn": "Quay lại điểm lấy hàng",
                "name_en_us": "Return to pick up location",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_round_trip.png",
                "img_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_round_trip.png",
                "order": 5,
                "description_vi_vn": "Tài xế sẽ quay lại điểm lấy hàng với cước phí bằng 50% phí khoảng cách. Lưu ý: Phí khoảng cách là cước phí dựa theo số km vận chuyển, không bao gồm phí điểm dừng và các loại phí khác.",
                "description_en_us": "Driver will return to pick up location for 50% of distance fee. Note: Distance fee is calculated solely by the travel distance, it does not include stop fee and others fee",
                "type": "COMMISSION_DISTANCE_PERCENTAGE",
                "price": 0.5,
                "description": "",
                "enable": True,
                "service_id": "SGN-PICKUP-TRUCK",
                "supplier_description_vi_vn": "Đối tác tiến hành quay trở lại điểm lấy hàng sau khi giao thành công ",
                "supplier_description": "Đối tác tiến hành quay trở lại điểm lấy hàng sau khi giao thành công ",
                "supplier_description_url": "https://ahamove.com/dichvukemtheo",
                "service_group_id": "PICKUP TRUCK",
                "group_id": "ROUND-TRIP"
            },
            {
                "_id": "SGN-PICKUP-TRUCK-PHICHO",
                "name": "Phí chờ (60,000 VNĐ/giờ)",
                "name_vi_vn": "Phí chờ (60,000 VNĐ/giờ)",
                "enable": True,
                "name_en_us": "Waiting fee (60,000 VND/hour)",
                "icon_url": "https://ahamove.com/wp-content/uploads/2022/01/waiting.png",
                "img_url": "https://ahamove.com/wp-content/uploads/2022/01/waiting.png",
                "order": 6,
                "price": 60000,
                "no_commission": True,
                "description_vi_vn": "Vui lòng chọn phụ phí thời gian chờ tương ứng để khích lệ tài xế trong trường hợp khách hàng có mong muốn tài xế chờ lâu hơn 45 phút kể từ thời điểm tài xế đến nơi lấy hàng.",
                "description_en_us": "In case customers want the driver to wait longer tSGN 45 minutes from the time driver arrived, please choose the corresponding waiting fee to encourage the driver.",
                "max_input": 5,
                "type": "PER_UNIT",
                "description": "",
                "service_id": "SGN-PICKUP-TRUCK",
                "service_group_id": "PICKUP TRUCK",
                "group_id": "PHICHO"
            },
            {
                "_id": "SGN-PICKUP-TRUCK-TIP",
                "name": "Hỗ trợ tài xế",
                "enable": True,
                "name_vi_vn": "Hỗ trợ tài xế",
                "name_en_us": "Tipping",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/sr_tipping.png",
                "img_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/sr_tipping.png",
                "order": 7,
                "price": 10000,
                "max_input": 10,
                "description_vi_vn": "Hãy chọn dịch vụ này nếu bạn muốn hỗ trợ tài xế trong giờ cao điểm, khi thời tiết khó khăn, hoặc đơn giản là muốn thưởng thêm cho tài xế. Ngoài ra, tính năng này sẽ giúp cho đơn hàng của bạn được ưu tiên hơn trong thời gian cao điểm.",
                "no_commission": True,
                "description_en_us": "This will show your support or compliment to the driver, especially in rush hours, bad weather. Also, this feature will prioritize your request in peak time.",
                "type": "PER_UNIT",
                "description": "",
                "service_id": "SGN-PICKUP-TRUCK",
                "service_group_id": "PICKUP TRUCK",
                "group_id": "TIP"
            }
        ],
        "currency": "VND"
    },
    {
        "_id": "SGN-VAN-500",
        "commission_type": "PERCENTAGE",
        "require_to": True,
        "require_request": False,
        "notify_package_return": False,
        "cross_service": {
            "enable": True,
            "services": [
                "SGN-TRICYCLE",
                "SGN-TRUCK-1000",
                "SGN-TRUCK-500",
                "SGN-VAN-500",
                "SGN-VAN-1000"
            ]
        },
        "parent_id": "",
        "city_id": "SGN",
        "recommendation_config": {
            "supplier_timeout": 30,
            "recommend_timeout": 90,
            "recommend_radius": 2500,
            "sleep_interval": 90,
            "dispatch_mode": "RECOMMEND",
            "pool_mode": "NO_POOL",
            "pool_saving_threshold": 0.2,
            "poolable": False
        },
        "vehicle_info": {
            "image": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/services/truck/Van-500.png",
            "length": 1.6,
            "width": 1.4,
            "height": 1.2,
            "weight": 500.0,
            "short_intro_vi": "Thích hợp xuống hầm chung cư và có thể di chuyển trong khung giờ cấm tải",
            "short_intro_en": "This vehicle is suitable to move down the basement apartment and moving in banned hours",
            "short_description_vi": "1.4 x 1.4 x 1.0 mét. Lên tới 500kg",
            "short_description_en": "1.4 x 2.4 x 1.0 Meter. Up to 500kgs",
            "box_volume": 10,
            "description_vi_vn": "Khối lượng chuyên chở: 500kg\nHàng hoá phù hợp (DxRxC): 1.6 x 1.4 x 1.2  mét\n\nPhí quãng đường:\n- Từ 00 - 04km: 185,000đ\n- Từ 04 - 10km: 20,000đ/km\n- Từ 10 - 15km: 14,375đ/km\n- Trên 15km: 14,000đ/km\n\nMức COD tối đa: 10,000,000đ\nPhí COD:\n- COD <   2,000,000đ: Miễn phí\n- COD >= 2,000,000đ: 0.8% x Giá trị COD",
            "description_en_us": "Payload capacity: 500kg\nSuitable goods (LxWxH): 1.6 x 1.4 x 1.2 meters\n\nDistance fee:\n- From 00 - 04km: 185,000 VND\n- From 04 - 10km: 20,000 VND/km\n- From 10 - 15km: 14,375 VND/km\n- Over 15km: 14,000 VND/km\n\nMaximum COD: 10,000,000 VND\nCOD fee:\n- COD <   2,000,000 VND: Free\n- COD >= 2,000,000 VND: 0.8% x Value of COD"
        },
        "name": "Xe VAN 500kg",
        "rebroadcast_interval": 1200,
        "rebroadcast_limit": 3,
        "name_vi_vn": "Xe VAN 500kg",
        "name_en_us": "Xe VAN 500kg",
        "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/services/truck/Van-500.png",
        "map_icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/tv-truck-1000.png",
        "order": 8,
        "broadcast_distance": 3000,
        "advance_broadcast_distance": 14500,
        "stop_fee": 11000,
        "timeout": 1800,
        "accept_interval": 1800,
        "max_stop_points": 10,
        "cod": 10000000,
        "max_cod": 10000000,
        "cod_commission": {
            "value": 0.008,
            "none_commission_limit": 2000000
        },
        "distance_fee_v3": {
            "blocks": [
                {
                    "from": 0,
                    "to": 4,
                    "base": 185000,
                    "price_multiplier": 0
                },
                {
                    "from": 4,
                    "to": 10,
                    "base": 185000,
                    "price_multiplier": 22000
                },
                {
                    "from": 10,
                    "to": 15,
                    "base": 317000,
                    "price_multiplier": 16000
                },
                {
                    "from": 15,
                    "to": 100000,
                    "base": 397000,
                    "price_multiplier": 15500
                }
            ],
            "hour_rates": []
        },
        "distance_fee": "185000 if x <= 4 else 185000 + (x - 4) * 22000 if x <= 10 else 185000 + 6 * 22000 + (x - 10) * 16000 if x <= 15 else 185000 + 6 * 22000 + 5 * 16000  + (x - 15) * 15500",
        "commission_value": 0.212,
        "enable": True,
        "description_en_us": "📦 (LxWxH) 1.6 x 1.4 x 1.2 meters",
        "description_vi_vn": "📦 (DxRxC) 1.6 x 1.4 x 1.2 mét",
        "`": "",
        "fee_description_vi_vn": "Khối lượng chuyên chở: 500kg\nHàng hoá phù hợp (DxRxC): 1.6 x 1.4 x 1.2  mét\n\nPhí quãng đường:\n- Từ 00 - 04km: 185,000đ\n- Từ 04 - 10km: 20,000đ/km\n- Từ 10 - 15km: 14,375đ/km\n- Trên 15km: 14,000đ/km\n\nMức COD tối đa: 10,000,000đ\nPhí COD:\n- COD <   2,000,000đ: Miễn phí\n- COD >= 2,000,000đ: 0.8% x Giá trị COD",
        "fee_description_en_us": "Payload capacity: 500kg\nSuitable goods (LxWxH): 1.6 x 1.4 x 1.2 meters\n\nDistance fee:\n- From 00 - 04km: 185,000 VND\n- From 04 - 10km: 20,000 VND/km\n- From 10 - 15km: 14,375 VND/km\n- Over 15km: 14,000 VND/km\n\nMaximum COD: 10,000,000 VND\nCOD fee:\n- COD <   2,000,000 VND: Free\n- COD >= 2,000,000 VND: 0.8% x Value of COD",
        "available_districts": [
            "VN.HC.BC",
            "VN.HC.CC",
            "VN.HC.CG",
            "VN.HC.HM",
            "VN.HC.NB",
            "VN.HC.BH",
            "VN.HC.BT",
            "VN.HC.GV",
            "VN.HC.PN",
            "VN.HC.QJ",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.QA",
            "VN.HC.QB",
            "VN.HC.QC",
            "VN.HC.QD",
            "VN.HC.QE",
            "VN.HC.QF",
            "VN.HC.QG",
            "VN.HC.QH",
            "VN.HC.QI",
            "VN.HC.TB",
            "VN.HC.TP",
            "VN.HC.TD"
        ],
        "delivery_type": "TRUCK",
        "enable_platform": [
            "momo_deeplink",
            "momo_permission",
            "zalo",
            "zalopay",
            "smartpay_deeplink",
            "viettel-pay_deeplink"
        ],
        "require_pod": True,
        "advance_max_concurrent_orders": 1,
        "max_concurrent_orders": 1,
        "group_name_en_us": "Tải trọng nhỏ",
        "group_name_vi_vn": "Tải trọng nhỏ",
        "supplier_description": "Thực hiện dưới 90 phút, nhận tối đa 1 đơn",
        "supplier_description_url": "https://ahamove.com/dich-vu-ba-gac-tai-tai-van/",
        "enable_cancellation_punishment": False,
        "vat_rate": 0.1,
        "truck_ban": {
            "ban_districts": [
                {
                    "_id": 260,
                    "hasc_2": "VN.HC.BH",
                    "name_2": "Bình Thạnh",
                    "city_id": "SGN",
                    "name": "BH",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 26
                },
                {
                    "_id": 267,
                    "hasc_2": "VN.HC.PN",
                    "name_2": "Phú Nhuận",
                    "city_id": "SGN",
                    "name": "PN",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 29
                },
                {
                    "_id": 268,
                    "hasc_2": "VN.HC.QJ",
                    "name_2": "Quận 10",
                    "city_id": "SGN",
                    "name": "QJ",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 30
                },
                {
                    "_id": 269,
                    "hasc_2": "VN.HC.QK",
                    "name_2": "Quận 11",
                    "city_id": "SGN",
                    "name": "QK",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 31
                },
                {
                    "_id": 270,
                    "hasc_2": "VN.HC.QL",
                    "name_2": "Quận 12",
                    "city_id": "SGN",
                    "name": "QL",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 32
                },
                {
                    "_id": 271,
                    "hasc_2": "VN.HC.QA",
                    "name_2": "Quận 1",
                    "city_id": "SGN",
                    "name": "QA",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 33
                },
                {
                    "_id": 273,
                    "hasc_2": "VN.HC.QC",
                    "name_2": "Quận 3",
                    "city_id": "SGN",
                    "name": "QC",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 35
                },
                {
                    "_id": 274,
                    "hasc_2": "VN.HC.QD",
                    "name_2": "Quận 4",
                    "city_id": "SGN",
                    "name": "QD",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 36
                },
                {
                    "_id": 275,
                    "hasc_2": "VN.HC.QE",
                    "name_2": "Quận 5",
                    "city_id": "SGN",
                    "name": "QE",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 37
                },
                {
                    "_id": 276,
                    "hasc_2": "VN.HC.QF",
                    "name_2": "Quận 6",
                    "city_id": "SGN",
                    "name": "QF",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 38
                },
                {
                    "_id": 277,
                    "hasc_2": "VN.HC.QG",
                    "name_2": "Quận 7",
                    "city_id": "SGN",
                    "name": "QG",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 39
                },
                {
                    "_id": 278,
                    "hasc_2": "VN.HC.QH",
                    "name_2": "Quận 8",
                    "city_id": "SGN",
                    "name": "QH",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 40
                },
                {
                    "_id": 280,
                    "hasc_2": "VN.HC.TB",
                    "name_2": "Tân Bình",
                    "city_id": "SGN",
                    "name": "TB",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 42
                }
            ],
            "recommend_service": "SGN-TRUCK-1000",
            "enable": True,
            "ban_hours": [
                {
                    "from": 0,
                    "to": 6
                },
                {
                    "from": 9,
                    "to": 21
                }
            ]
        },
        "priority_score": 6,
        "alternative_vehicles": [
            "TRICYCLE",
            "VAN-1000"
        ],
        "default_vehicles": [
            "VAN-500"
        ],
        "is_select_vehicle_allowed": True,
        "group_id": "VAN-500",
        "animated_url": "https://i.imgur.com/xiDxEYN.png",
        "requests": [
            {
                "_id": "SGN-VAN-500-BOCXEP-KLLMC",
                "name": "Bốc xếp không lên lầu - 1 chiều",
                "name_vi_vn": "Bốc xếp không lên lầu - 1 chiều",
                "enable": True,
                "name_en_us": "1 Way moving help (ground floor only)",
                "icon_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_loading_per_helper.png",
                "img_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_loading_per_helper.png",
                "order": 1,
                "price": 50000,
                "description_vi_vn": "Tài xế hỗ trợ bốc xếp hàng hóa (đã được đóng thùng) xuống xe đến địa điểm chỉ định trong vòng 100m HOẶC ngược lại (Áp dụng cho 1 lượt và không lên lầu). Các trường hợp phát sinh thêm, vui lòng thoả thuận với tài xế.",
                "description_en_us": "Driver provides moving help (already packaged) from vehicle to designated location within 100m OR vice versa (Apply for 1 turn and ground floor only). For additional cases, please negotiate with the driver.",
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-VAN-500",
                "category": "UNLOADING",
                "service_group_id": "VAN-500",
                "group_id": "BOCXEP"
            },
            {
                "_id": "SGN-VAN-500-CHUYENNHA",
                "name": "Gói hỗ trợ chuyển nhà cơ bản",
                "name_vi_vn": "Gói hỗ trợ chuyển nhà cơ bản",
                "name_en_us": "Gói hỗ trợ chuyển nhà cơ bản",
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/house-moving.png",
                "order": 1,
                "price": 300000,
                "description_vi_vn": "Chi tiết gói: \n- Hỗ trợ bốc xếp: 240000\n- Phí chờ: 60000\n \n Lưu ý: \n- Địa hình vận chuyển: Không quá 100m và 2 tầng/ lầu tại 2 chiều.\n- Vui lòng tháo lắp đồ điện lạnh, nội thất và đóng gói hàng hoá trước khi đặt dịch vụ\n- Trường hợp có phát sinh cước luân chuyển, bốc xếp vui lòng liên hệ tổng đài 1900545411 để được xác nhận.",
                "description_en_us": "Chi tiết gói: \n- Hỗ trợ bốc xếp: 240000\n- Phí chờ: 60000\n \n Lưu ý: \n- Địa hình vận chuyển: Không quá 100m và 2 tầng/ lầu tại 2 chiều.\n- Vui lòng tháo lắp đồ điện lạnh, nội thất và đóng gói hàng hoá trước khi đặt dịch vụ\n- Trường hợp có phát sinh cước luân chuyển, bốc xếp vui lòng liên hệ tổng đài 1900545411 để được xác nhận.",
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-VAN-500",
                "img_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/house-moving.png",
                "enable": True,
                "options": [
                    {
                        "code": "ITEM_1",
                        "name_vi_vn": "Hỗ trợ bốc xếp",
                        "name_en_us": "Hỗ trợ bốc xếp",
                        "selectable": True
                    },
                    {
                        "code": "ITEM_2",
                        "name_vi_vn": "Phí chờ",
                        "name_en_us": "Phí chờ",
                        "selectable": True
                    },
                    {
                        "code": "ITEM_3",
                        "name_vi_vn": "Combo Bốc xếp và phí chờ",
                        "name_en_us": "Combo Bốc xếp và phí chờ",
                        "selectable": True
                    }
                ],
                "service_group_id": "VAN-500",
                "group_id": "CHUYENNHA"
            },
            {
                "_id": "SGN-VAN-500-INSURANCE",
                "name": "Khai giá hàng hoá",
                "name_vi_vn": "Khai giá hàng hoá",
                "name_en_us": "Value declaration",
                "enable": True,
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/Insurance/secure+24x24%402x.png",
                "order": 1,
                "price_blocks": [
                    {
                        "from": 0,
                        "to": 10000001,
                        "price": 2000,
                        "description_vi_vn": "Bồi thường mất mát hoặc hư hỏng theo giá trị hàng hoá của bạn",
                        "description_en_us": "Coverage for loss or damage according to the value of your items"
                    }
                ],
                "no_supplier_payout": True,
                "type": "COD_INSURANCE",
                "applied_stp_num": 10,
                "required_item_value": True,
                "service_id": "SGN-VAN-500",
                "description_url": "https://ahamove.com/phi-khai-gia-cho-truck-ahmxsaladin/",
                "benefit_url": "https://ahamove.com/phi-khai-gia-cho-truck-ahmxsaladin/",
                "non_cod_description": "Bồi thường mất mát hoặc hư hỏng theo danh mục hàng hoá của bạn",
                "none_cod_price_blocks": {
                    "electronics": 2000,
                    "health & beauty": 2000,
                    "housing & lifestyle": 2000,
                    "food": 2000,
                    "mother & baby": 2000,
                    "fashion": 2000,
                    "grocery": 2000,
                    "restaurant": 2000,
                    "sport": 2000,
                    "drink": 2000,
                    "other": 2000,
                    "individual needs": 2000,
                    "transportation": 2000
                },
                "service_group_id": "VAN-500"
            },
            {
                "_id": "SGN-VAN-500-BOCXEP-KLLHC",
                "name": "Bốc xếp không lên lầu - 2 chiều",
                "enable": True,
                "name_vi_vn": "Bốc xếp không lên lầu - 2 chiều",
                "name_en_us": "2 Ways moving help (ground floor only)",
                "icon_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_loading_per_helper.png",
                "img_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_loading_per_helper.png",
                "order": 2,
                "price": 77000,
                "description_vi_vn": "Tài xế hỗ trợ bốc xếp hàng hóa (đã được đóng thùng) xuống xe đến địa điểm chỉ định trong vòng 100m VÀ ngược lại (Áp dụng cho 2 lượt và không lên lầu). Các trường hợp phát sinh thêm, vui lòng thoả thuận với tài xế.",
                "description_en_us": "Driver provides moving help (already packaged) from vehicle to designated location within 100m AND vice versa (Apply for 2 turns and ground floor only). For additional cases, please negotiate with the driver.",
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-VAN-500",
                "category": "UNLOADING",
                "service_group_id": "VAN-500",
                "group_id": "BOCXEP"
            },
            {
                "_id": "SGN-VAN-500-LOADERS",
                "name": "Thêm người bốc xếp",
                "enable": True,
                "name_vi_vn": "Thêm người bốc xếp",
                "name_en_us": "Thêm người bốc xếp",
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/more-pickers.png",
                "img_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/more-pickers.png",
                "order": 2,
                "price": 300000,
                "max_input": 3,
                "description_vi_vn": "Hàng hoá số lượng lớn hay có kích thước cồng kềnh, nặng và yêu cầu phải có 2 người bưng trở lên",
                "no_commission": False,
                "description_en_us": "Hàng hoá số lượng lớn hay có kích thước cồng kềnh, nặng và yêu cầu phải có 2 người bưng trở lên",
                "type": "PER_UNIT",
                "description": "Hàng hoá số lượng lớn hay có kích thước cồng kềnh, nặng và yêu cầu phải có 2 người bưng trở lên",
                "service_id": "SGN-VAN-500",
                "service_group_id": "VAN-500",
                "group_id": "LOADER"
            },
            {
                "_id": "SGN-VAN-500-BOCXEP-LLMC",
                "name": "Bốc xếp tại nhà có lầu - 1 chiều",
                "name_vi_vn": "Bốc xếp tại nhà có lầu - 1 chiều",
                "enable": True,
                "name_en_us": "1 Way moving help (Maximum 1 Floor)",
                "icon_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_moving_help_upstair.png",
                "img_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_moving_help_upstair.png",
                "order": 3,
                "price": 110000,
                "description_vi_vn": "Tài xế hỗ trợ bốc xếp hàng hóa (đã được đóng thùng) xuống xe đến địa điểm chỉ định trong vòng 100m HOẶC ngược lại (Áp dụng cho 1 lượt, 1 lầu). Các trường hợp phát sinh thêm, vui lòng thoả thuận với tài xế.",
                "description_en_us": "Driver provides moving help (already packaged) from vehicle to designated location within 100m OR vice versa (Apply for 1 turn and maximum 1 floor). For additional cases, please negotiate with the driver.",
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-VAN-500",
                "category": "UNLOADING",
                "service_group_id": "VAN-500",
                "group_id": "BOCXEP"
            },
            {
                "_id": "SGN-VAN-500-BOCXEP-LLHC",
                "name": "Bốc xếp tại nhà có lầu - 2 chiều",
                "name_vi_vn": "Bốc xếp tại nhà có lầu - 2 chiều",
                "enable": True,
                "name_en_us": "2 Ways moving help (Maximum 1 Floor)",
                "icon_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_moving_help_upstair.png",
                "img_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_moving_help_upstair.png",
                "order": 4,
                "price": 165000,
                "description_vi_vn": "Tài xế hỗ trợ bốc xếp hàng hóa (đã được đóng thùng) xuống xe đến địa điểm chỉ định trong vòng 100m VÀ ngược lại (Áp dụng cho 2 lượt, 1 lầu). Các trường hợp phát sinh thêm, vui lòng thoả thuận với tài xế.",
                "description_en_us": "Driver provides moving help (already packaged) from vehicle to designated location within 100m AND vice versa (Apply for 1 turn and maximum 1 floor). For additional cases, please negotiate with the driver.",
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-VAN-500",
                "category": "UNLOADING",
                "service_group_id": "VAN-500",
                "group_id": "BOCXEP"
            },
            {
                "_id": "SGN-VAN-500-ROUND-TRIP",
                "name": "Quay lại điểm lấy hàng",
                "enable": True,
                "name_vi_vn": "Quay lại điểm lấy hàng",
                "name_en_us": "Return to pick up location",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_round_trip.png",
                "img_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_round_trip.png",
                "order": 5,
                "description_vi_vn": "Tài xế sẽ quay lại điểm lấy hàng với cước phí bằng 50% phí khoảng cách. Lưu ý: Phí khoảng cách là cước phí dựa theo số km vận chuyển, không bao gồm phí điểm dừng và các loại phí khác.",
                "description_en_us": "Driver will return to pick up location for 50% of distance fee. Note: Distance fee is calculated solely by the travel distance, it does not include stop fee and others fee",
                "type": "COMMISSION_DISTANCE_PERCENTAGE",
                "price": 0.5,
                "description": "",
                "service_id": "SGN-VAN-500",
                "service_group_id": "VAN-500",
                "group_id": "ROUND-TRIP"
            },
            {
                "_id": "SGN-VAN-500-TIP",
                "name": "Hỗ trợ tài xế",
                "enable": True,
                "name_vi_vn": "Hỗ trợ tài xế",
                "name_en_us": "Tipping",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/sr_tipping.png",
                "img_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/sr_tipping.png",
                "order": 8,
                "price": 10000,
                "max_input": 10,
                "no_commission": True,
                "description_vi_vn": "Hãy chọn dịch vụ này nếu bạn muốn hỗ trợ tài xế trong giờ cao điểm, khi thời tiết khó khăn, hoặc đơn giản là muốn thưởng thêm cho tài xế. Ngoài ra, tính năng này sẽ giúp cho đơn hàng của bạn được ưu tiên hơn trong thời gian cao điểm.",
                "description_en_us": "This will show your support or compliment to the driver, especially in rush hours, bad weather. Also, this feature will prioritize your request in peak time.",
                "type": "PER_UNIT",
                "description": "",
                "service_id": "SGN-VAN-500",
                "group_id": "TIP",
                "service_group_id": "VAN-500"
            }
        ],
        "currency": "VND"
    },
    {
        "_id": "SGN-HUB-SE",
        "commission_type": "PERCENTAGE",
        "require_to": True,
        "require_request": False,
        "parent_id": "",
        "city_id": "SGN",
        "name": "HUB Cồng Kềnh",
        "name_vi_vn": "HUB Cồng Kềnh",
        "name_en_us": "HUB Bulky",
        "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/sp-hub.png",
        "map_icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/tv-bike.png",
        "order": 8,
        "broadcast_distance": 7000,
        "advance_broadcast_distance": 7000,
        "stop_fee": 22000,
        "stop_failed": 22000,
        "enable": True,
        "timeout": 36000,
        "accept_interval": 1800,
        "max_stop_points": 21,
        "distance_fee": "0",
        "commission_value": 0.3105,
        "require_pod": False,
        "location": [
            {
                "lng": 106.664025,
                "lat": 10.769967
            },
            {
                "lng": 106.657038,
                "lat": 10.7726336
            },
            {
                "lng": 106.7001281,
                "lat": 10.7571664
            },
            {
                "lng": 106.6612372,
                "lat": 10.8009098
            },
            {
                "lng": 106.694785,
                "lat": 10.7690426
            },
            {
                "lng": 106.7120955,
                "lat": 10.8098009
            },
            {
                "lng": 106.6867061,
                "lat": 10.7706871
            },
            {
                "lng": 106.693248,
                "lat": 10.760305
            },
            {
                "lng": 106.7135168,
                "lat": 10.7986618
            },
            {
                "lng": 106.7135889,
                "lat": 10.798822
            },
            {
                "lng": 106.71303,
                "lat": 10.7986485
            },
            {
                "lng": 106.701583,
                "lat": 10.745586
            },
            {
                "lng": 106.6111886,
                "lat": 10.8176126
            },
            {
                "lng": 106.6107746,
                "lat": 10.8198324
            },
            {
                "lng": 106.6127303,
                "lat": 10.8198501
            },
            {
                "lng": 106.6202069,
                "lat": 10.8040739
            },
            {
                "lng": 106.6649492,
                "lat": 10.8485407
            },
            {
                "lng": 106.6164587,
                "lat": 10.8069437
            },
            {
                "lng": 106.6663901,
                "lat": 10.8488272
            },
            {
                "lng": 106.6211575,
                "lat": 10.8066531
            },
            {
                "lng": 106.6666894,
                "lat": 10.84881
            },
            {
                "lng": 106.6171609,
                "lat": 10.807021
            },
            {
                "lng": 106.6159155,
                "lat": 10.8087893
            },
            {
                "lng": 106.616526,
                "lat": 10.808233
            }
        ],
        "vat_rate": 0.1,
        "available_districts": [
            "VN.HC.NB",
            "VN.HC.CG",
            "VN.HC.CC",
            "VN.HC.BC",
            "VN.HC.HM",
            "VN.BH",
            "VN.CM",
            "VN.LT",
            "VN.TDM",
            "VN.PG",
            "VN.TA",
            "VN.BC",
            "VN.BB",
            "VN.LK",
            "VN.XL",
            "VN.TP",
            "VN.VC",
            "VN.VT.TT",
            "VN.VT.XM",
            "VN.VT.DD",
            "VN.VT.VT",
            "VN.VT.BR",
            "VN.VT.CD",
            "VN.VT.CD",
            "VN.VT.LD",
            "VN.DA",
            "VN.HC.QB",
            "VN.HC.QC",
            "VN.HC.QG",
            "VN.HC.BH",
            "VN.HC.GV",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.PN",
            "VN.HC.QJ",
            "VN.HC.QD",
            "VN.HC.BT",
            "VN.HC.QF",
            "VN.HC.QA",
            "VN.HC.QE",
            "VN.HC.TB",
            "VN.HC.TD",
            "VN.HC.QH",
            "VN.HC.QI",
            "VN.HC.TP"
        ],
        "drop_off_districts": [
            "VN.HC.NB",
            "VN.HC.CG",
            "VN.HC.CC",
            "VN.HC.BC",
            "VN.HC.HM",
            "VN.BH",
            "VN.CM",
            "VN.LT",
            "VN.TDM",
            "VN.PG",
            "VN.TA",
            "VN.BC",
            "VN.BB",
            "VN.LK",
            "VN.XL",
            "VN.TP",
            "VN.VC",
            "VN.VT.TT",
            "VN.VT.XM",
            "VN.VT.DD",
            "VN.VT.VT",
            "VN.VT.BR",
            "VN.VT.CD",
            "VN.VT.CD",
            "VN.VT.LD",
            "VN.DA",
            "VN.HC.QB",
            "VN.HC.QC",
            "VN.HC.QG",
            "VN.HC.BH",
            "VN.HC.GV",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.PN",
            "VN.HC.QJ",
            "VN.HC.QD",
            "VN.HC.BT",
            "VN.HC.QF",
            "VN.HC.QA",
            "VN.HC.QE",
            "VN.HC.TB",
            "VN.HC.TD",
            "VN.HC.QH",
            "VN.HC.QI",
            "VN.HC.TP"
        ],
        "max_cod": 50000000,
        "cod": 50000000,
        "priority_score": 6,
        "distance_fee_v3": {
            "blocks": [
                {
                    "from": 0,
                    "to": 100000,
                    "base": 0,
                    "price_multiplier": 0
                }
            ],
            "hour_rates": []
        },
        "group_id": "HUB-SE",
        "animated_url": "https://i.imgur.com/xiDxEYN.png",
        "requests": [
            {
                "_id": "SGN-HUB-SE-TRANSFER-COD",
                "name": "Thu hộ COD",
                "enable": True,
                "name_vi_vn": "Thu hộ COD",
                "name_en_us": "Collect COD",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_d2d.png",
                "order": 1,
                "price": 0,
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-HUB-SE",
                "no_commission": True,
                "service_group_id": "HUB-SE",
                "group_id": "TRANSFER_COD"
            }
        ],
        "currency": "VND"
    },
    {
        "_id": "SGN-FOOD",
        "enable": True,
        "order": 10,
        "city_id": "SGN",
        "timeout": 1800,
        "rebroadcast_interval": 1200,
        "name": "Giao Đồ Ăn",
        "broadcast_distance": 50000,
        "name_vi_vn": "Giao Đồ Ăn",
        "icon_url": "https://i.imgur.com/HLJclQY.png",
        "map_icon_url": "https://i.imgur.com/rPuT8pk.png",
        "parent_id": "",
        "commission_type": "PERCENTAGE",
        "commission_value": 0.236,
        "distance_fee": "(20000 if x <= 2 else 20000 + (x - 2) * 5500)",
        "vat_rate": 0.1,
        "stop_fee": 5000,
        "name_en_us": "FOOD",
        "require_to": True,
        "auto_assign": False,
        "cod": 10000000,
        "first_order_cod": 1,
        "advance_broadcast_distance": 100000,
        "max_stop_points": 1,
        "pool_timeout": 6300,
        "pool_timeout_commission_value": 0.3,
        "max_concurrent_orders": 2,
        "fee_description_en_us": "Minimum fee (within 6km): đ30,000\nPer km: đ5,000",
        "description_en_us": "Deliver within an hour",
        "description_vi_vn": "Giao hàng trong Giao hàng trong 1h",
        "auto_assign_distance": 50000,
        "partner": True,
        "require_cod": True,
        "tooltips": {
            "PAYING": {
                "message": [
                    "Please pay for this order to continue"
                ],
                "message_vi_vn": [
                    "Vui lòng thanh toán đơn hàng để tiếp tục"
                ]
            },
            "CONFIRMING": {
                "message": [
                    "Plase wait for the restaurant to confirm your order\n             "
                ],
                "message_vi_vn": [
                    "Vui lòng đợi xác nhận từ nhà hàng"
                ]
            },
            "ASSIGNING": {
                "message": [
                    "We are finding a driver to deliver this order"
                ],
                "message_vi_vn": [
                    "Chúng tôi đang tìm tài xế để thực hiện đơn hàng này"
                ]
            },
            "ACCEPTED": {
                "message": [
                    "Driver will pick up your order within 15 minutes"
                ],
                "message_vi_vn": [
                    "Tài xế sẽ đến chỗ nhận hàng trong vòng 15 phút"
                ]
            }
        },
        "fee_description_vi_vn": "Phí tối thiểu (dưới 6km): đ30,000\nCác km tiếp theo: đ5,000",
        "supplier_description": "https://ahamove.com/quy-trinh-giao-don-do-an/",
        "cross_service": {
            "enable": False,
            "services": []
        },
        "note": "- ỨNG THEO SỐ TIỀN TRÊN APP",
        "cross_city": {
            "enable": True,
            "cities": [
                "SGN",
                "BHC",
                "THD",
                "VTG"
            ]
        },
        "available_districts": [
            "VN.HC.NB",
            "VN.HC.CG",
            "VN.HC.CC",
            "VN.HC.BC",
            "VN.HC.HM",
            "VN.BH",
            "VN.CM",
            "VN.LT",
            "VN.TDM",
            "VN.TA",
            "VN.LK",
            "VN.XL",
            "VN.TP",
            "VN.VC",
            "VN.VT.VT",
            "VN.VT.BR",
            "VN.DA",
            "VN.HC.QB",
            "VN.HC.QC",
            "VN.HC.QG",
            "VN.HC.BH",
            "VN.HC.GV",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.PN",
            "VN.HC.QJ",
            "VN.HC.QD",
            "VN.HC.BT",
            "VN.HC.QF",
            "VN.HC.QA",
            "VN.HC.QE",
            "VN.HC.TB",
            "VN.HC.TD",
            "VN.HC.QH",
            "VN.HC.QI",
            "VN.HC.TP"
        ],
        "distance_fee_v3": {
            "blocks": [
                {
                    "from": 0,
                    "to": 2,
                    "base": 20000,
                    "price_multiplier": 0
                },
                {
                    "from": 2,
                    "to": 100000,
                    "base": 20000,
                    "price_multiplier": 5500
                }
            ],
            "hour_rates": []
        },
        "enable_platform": [
            "momo_deeplink",
            "momo_permission",
            "zalo",
            "zalopay",
            "smartpay_deeplink",
            "viettel-pay_deeplink",
            "shopee-pay_deeplink",
            "onwheel"
        ],
        "priority_score": 6,
        "group_id": "FOOD",
        "animated_url": "https://i.imgur.com/xiDxEYN.png",
        "requests": [
            {
                "_id": "SGN-FOOD-H2H",
                "name": "Hand-to-hand",
                "enable": True,
                "name_vi_vn": "Giao hàng lên lầu",
                "support_remarks": True,
                "name_en_us": "Upstair delivery",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_d2d.png",
                "order": 1,
                "price": 10000,
                "no_commission": True,
                "type": "BOOLEAN",
                "service_id": "SGN-FOOD",
                "img_url": "http://file.hstatic.net/1000010797/file/hand-to-hand.png",
                "description_vi_vn": "Khách hàng hỗ trợ chi phí giao hàng tận tay cho tài xế trong trường hợp các điểm giao thuộc chung cư,  cơ quan, bệnh viện,...Hãy chọn số lượng tương ứng với số điểm giao hàng bạn cần tài xế giao tận tay.",
                "description_en_us": "Customer can request driver for hand to hand delivery service if drop off point is an apartment, an office , a hospital or a building. Please select the number of drop off points that need hand to hand delivery.",
                "group_id": "H2H",
                "service_group_id": "FOOD"
            },
            {
                "_id": "SGN-FOOD-ITEM",
                "name": "ITEM3K",
                "enable": True,
                "name_vi_vn": "ITEM3K",
                "name_en_us": "ITEM3K",
                "price": 0,
                "item_price": 3000,
                "max_input": 1,
                "min_input": 1,
                "icon_url": "https://i.imgur.com/HLJclQY.png",
                "img_url": "https://i.imgur.com/HLJclQY.png",
                "order": 1,
                "type": "ITEM",
                "description": "",
                "service_id": "SGN-FOOD"
            }
        ],
        "currency": "VND"
    },
    {
        "_id": "SGN-HUB",
        "commission_type": "PERCENTAGE",
        "require_to": True,
        "require_request": False,
        "parent_id": "",
        "city_id": "SGN",
        "enable": True,
        "name": "HUB",
        "name_vi_vn": "HUB",
        "need_confirm_before_pickup": True,
        "name_en_us": "HUB",
        "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/sp_hub.png",
        "map_icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/tv_motorcycle.png",
        "order": 10,
        "broadcast_distance": 5000,
        "stop_fee": 5000,
        "distance_fee": "30000 if x <= 6 else 30000 + (x - 6) * 5000",
        "commission_value": 0.3,
        "accept_interval": 1800,
        "timeout": 1800,
        "cod": 50000000,
        "stop_failed": 5000,
        "require_pod": True,
        "advance_broadcast_distance": 5000,
        "partner": True,
        "max_concurrent_orders": 3,
        "cross_service": {
            "enable": False,
            "services": []
        },
        "max_stop_points": 21,
        "delivery_type": "HUB",
        "max_cod": 50000000,
        "priority_score": 1,
        "distance_fee_v3": {
            "blocks": [
                {
                    "from": 0,
                    "to": 6,
                    "base": 30000,
                    "price_multiplier": 0
                },
                {
                    "from": 6,
                    "to": 100000,
                    "base": 30000,
                    "price_multiplier": 5000
                }
            ],
            "hour_rates": []
        },
        "group_id": "HUB",
        "animated_url": "https://i.imgur.com/xiDxEYN.png",
        "requests": [],
        "currency": "VND"
    },
    {
        "_id": "SGN-VAN-1000",
        "commission_type": "PERCENTAGE",
        "require_to": True,
        "require_request": False,
        "notify_package_return": False,
        "cross_service": {
            "enable": True,
            "services": [
                "SGN-TRICYCLE",
                "SGN-TRUCK-1000",
                "SGN-TRUCK-500",
                "SGN-VAN-500",
                "SGN-VAN-1000"
            ]
        },
        "parent_id": "",
        "city_id": "SGN",
        "recommendation_config": {
            "supplier_timeout": 30,
            "recommend_timeout": 90,
            "recommend_radius": 3500,
            "sleep_interval": 90,
            "dispatch_mode": "RECOMMEND",
            "pool_mode": "NO_POOL",
            "pool_saving_threshold": 0.2,
            "poolable": False
        },
        "name": "Xe VAN 1000kg",
        "rebroadcast_interval": 1200,
        "rebroadcast_limit": 3,
        "name_vi_vn": "Xe VAN 1000kg",
        "name_en_us": "Xe VAN 1000kg",
        "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/services/truck/Van-1000.png",
        "map_icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/tv-truck-1000.png",
        "order": 10,
        "enable": True,
        "broadcast_distance": 3500,
        "advance_broadcast_distance": 15500,
        "stop_fee": 22000,
        "timeout": 1800,
        "accept_interval": 1800,
        "max_stop_points": 10,
        "cod": 10000000,
        "max_cod": 10000000,
        "cod_commission": {
            "value": 0.008,
            "none_commission_limit": 2000000
        },
        "distance_fee": "245000 if x <= 4 else 245000 + (x - 4) * 28500 if x <= 15 else 245000 + 11 * 28500 + (x - 15) * 24500",
        "commission_value": 0.212,
        "description_en_us": "📦 (LxWxH) 2 x 1.5 x 1.5 meters",
        "description_vi_vn": "📦 (DxRxC) 2 x 1.5 x 1.5 mét",
        "fee_description_vi_vn": "Khối lượng chuyên chở: 900 kg\nHàng hoá phù hợp (DxRxC): 2 x 1.5 x 1.5 mét\n\nPhí quãng đường:\n- Từ 00 - 04km: 245,000đ\n- Từ 04 - 15km: 26,000đ/km\n- Trên 15km: 22,000đ/km\n\nMức COD tối đa: 10,000,000đ\nPhí COD:\n- COD <   2,000,000đ: Miễn phí\n- COD >= 2,000,000đ: 0.8% x Giá trị COD",
        "fee_description_en_us": "Payload capacity: 900 kg\nSuitable goods (LxWxH): 2 x 1.5 x 1.5 meters\n\nDistance fee:\n- From 00 - 04km: 245,000 VND\n- From 04 - 15km: 26,000 VND/km\n- Over 15km: 22,000 VND/km\n\nMaximum COD: 10,000,000 VND\nCOD fee:\n- COD <   2,000,000 VND: Free\n- COD >= 2,000,000 VND: 0.8% x Value of COD",
        "available_districts": [
            "VN.HC.BC",
            "VN.HC.CC",
            "VN.HC.CG",
            "VN.HC.HM",
            "VN.HC.NB",
            "VN.TDM",
            "VN.BH",
            "VN.LT",
            "VN.TA",
            "VN.DA",
            "VN.NT",
            "VN.TB",
            "VN.HC.BH",
            "VN.HC.BT",
            "VN.HC.GV",
            "VN.HC.PN",
            "VN.HC.QJ",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.QA",
            "VN.HC.QC",
            "VN.HC.QD",
            "VN.HC.QE",
            "VN.HC.QF",
            "VN.HC.QG",
            "VN.HC.QH",
            "VN.HC.TB",
            "VN.HC.TP",
            "VN.HC.TD"
        ],
        "delivery_type": "TRUCK",
        "enable_platform": [
            "momo_deeplink",
            "momo_permission",
            "zalo",
            "zalopay",
            "smartpay_deeplink",
            "viettel-pay_deeplink"
        ],
        "max_cod_per_stop_point": 10000000,
        "advance_max_concurrent_orders": 1,
        "max_concurrent_orders": 1,
        "supplier_description": "Thực hiện dưới 90 phút, nhận tối đa 1 đơn",
        "supplier_description_url": "https://ahamove.com/dich-vu-ba-gac-tai-tai-van/",
        "enable_cancellation_punishment": False,
        "vat_rate": 0.1,
        "priority_score": 6,
        "vehicle_info": {
            "image": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/services/truck/Van-1000.png",
            "length": 2.0,
            "width": 1.5,
            "height": 1.5,
            "weight": 900.0,
            "short_intro_vi": "Thích hợp cho hàng hoá lớn và có thể di chuyển trong khung giờ cấm tải ",
            "short_intro_en": "This vehicle is suitable to carry big parcel and moving in banned hours",
            "short_description_vi": "2.0 x 1.5 x 1.5 mét. Lên tới 900kg",
            "short_description_en": "2.0 x 1.5 x 1.5 Meter. Up to 900kgs",
            "box_volume": 10.0,
            "description_vi_vn": "\"Khối lượng chuyên chở: 900 kg\nHàng hoá phù hợp (DxRxC): 2 x 1.5 x 1.5 mét\n\nPhí quãng đường:\n- Từ 00 - 04km: 245,000đ\n- Từ 04 - 15km: 28,500đ/km\n- Trên 15km: 24,500đ/km\n\nPhí điểm dừng: 22,000đ/điểm dừng\n\nMức COD tối đa: 10,000,000đ\nPhí COD:\n- COD <   2,000,000đ: Miễn phí\n- COD >= 2,000,000đ: 0.88% x Giá trị COD\"",
            "description_en_us": "\"Payload capacity: 900 kg\nSuitable goods (LxWxH): 2 x 1.5 x 1.5 meters\n\nDistance fee:\n- From 00 - 04km: 245,000 VND\n- From 04 - 15km: 28,500 VND/km\n- Over 15km: 24,500 VND/km\n\nStop-fee: 22,000 VND/stop\n\nMaximum COD: 10,000,000 VND\nCOD fee:\n- COD <   2,000,000 VND: Free\n- COD >= 2,000,000 VND: 0.88% x Value of COD\""
        },
        "distance_fee_v3": {
            "blocks": [
                {
                    "from": 0,
                    "to": 4,
                    "base": 245000,
                    "price_multiplier": 0
                },
                {
                    "from": 4,
                    "to": 15,
                    "base": 245000,
                    "price_multiplier": 28500
                },
                {
                    "from": 15,
                    "to": 100000,
                    "base": 558500,
                    "price_multiplier": 24500
                }
            ],
            "hour_rates": []
        },
        "group_id": "VAN-1000",
        "animated_url": "https://i.imgur.com/xiDxEYN.png",
        "requests": [
            {
                "_id": "SGN-VAN-1000-BOCXEP-KLLMC",
                "name": "Bốc xếp không lên lầu - 1 chiều",
                "enable": True,
                "name_vi_vn": "Bốc xếp không lên lầu - 1 chiều",
                "name_en_us": "1 Way moving help (ground floor only)",
                "icon_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_loading_per_helper.png",
                "img_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_loading_per_helper.png",
                "order": 1,
                "price": 110000,
                "description_vi_vn": "Tài xế hỗ trợ bốc xếp hàng hóa (đã được đóng thùng) xuống xe đến địa điểm chỉ định trong vòng 100m HOẶC ngược lại (Áp dụng cho 1 lượt và không lên lầu). Các trường hợp phát sinh thêm, vui lòng thoả thuận với tài xế.",
                "description_en_us": "Driver provides moving help (already packaged) from vehicle to designated location within 100m OR vice versa (Apply for 1 turn and ground floor only). For additional cases, please negotiate with the driver.",
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-VAN-1000",
                "category": "UNLOADING",
                "service_group_id": "VAN-1000",
                "group_id": "BOCXEP"
            },
            {
                "_id": "SGN-VAN-1000-CHUYENNHA",
                "name": "Gói hỗ trợ chuyển nhà cơ bản",
                "name_vi_vn": "Gói hỗ trợ chuyển nhà cơ bản",
                "name_en_us": "Gói hỗ trợ chuyển nhà cơ bản",
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/house-moving.png",
                "order": 1,
                "price": 600000,
                "description_vi_vn": "Chi tiết gói: \n- Thêm 1 người bốc xếp: 300000 \n- Hỗ trợ bốc xếp: 240000\n- Phí chờ: 60000\n \n Lưu ý: \n- Địa hình vận chuyển: Không quá 100m và 2 tầng/ lầu tại 2 chiều.\n- Vui lòng tháo lắp đồ điện lạnh, nội thất và đóng gói hàng hoá trước khi đặt dịch vụ\n- Trường hợp có phát sinh cước luân chuyển, bốc xếp vui lòng liên hệ tổng đài 1900545411 để được xác nhận.",
                "description_en_us": "Chi tiết gói: \n- Thêm 1 người bốc xếp: 300000 \n- Hỗ trợ bốc xếp: 240000\n- Phí chờ: 60000\n \n Lưu ý: \n- Địa hình vận chuyển: Không quá 100m và 2 tầng/ lầu tại 2 chiều.\n- Vui lòng tháo lắp đồ điện lạnh, nội thất và đóng gói hàng hoá trước khi đặt dịch vụ\n- Trường hợp có phát sinh cước luân chuyển, bốc xếp vui lòng liên hệ tổng đài 1900545411 để được xác nhận.",
                "type": "BOOLEAN",
                "description": "Chi tiết gói: \n- Thêm 1 người bốc xếp: 300000 \n- Hỗ trợ bốc xếp: 240000\n- Phí chờ: 60000\n \n Lưu ý: \n- Địa hình vận chuyển: Không quá 100m và 2 tầng/ lầu tại 2 chiều.\n- Vui lòng tháo lắp đồ điện lạnh, nội thất và đóng gói hàng hoá trước khi đặt dịch vụ\n- Trường hợp có phát sinh cước luân chuyển, bốc xếp vui lòng liên hệ tổng đài 1900545411 để được xác nhận.",
                "service_id": "SGN-VAN-1000",
                "img_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/house-moving.png",
                "enable": True,
                "options": [
                    {
                        "code": "ITEM_1",
                        "name_vi_vn": "Hỗ trợ bốc xếp (x2)",
                        "name_en_us": "Hỗ trợ bốc xếp (x2)",
                        "selectable": True
                    },
                    {
                        "code": "ITEM_2",
                        "name_vi_vn": "Phí chờ",
                        "name_en_us": "Phí chờ",
                        "selectable": True
                    },
                    {
                        "code": "ITEM_3",
                        "name_vi_vn": "Combo Bốc xếp và phí chờ",
                        "name_en_us": "Combo Bốc xếp và phí chờ",
                        "selectable": True
                    }
                ],
                "service_group_id": "VAN-1000",
                "group_id": "CHUYENNHA"
            },
            {
                "_id": "SGN-VAN-1000-INSURANCE",
                "name": "Khai giá hàng hoá",
                "name_vi_vn": "Khai giá hàng hoá",
                "name_en_us": "Value declaration",
                "enable": True,
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/Insurance/secure+24x24%402x.png",
                "order": 1,
                "price_blocks": [
                    {
                        "from": 0,
                        "to": 10000001,
                        "price": 2000,
                        "description_vi_vn": "Bồi thường mất mát hoặc hư hỏng theo giá trị hàng hoá của bạn",
                        "description_en_us": "Coverage for loss or damage according to the value of your items"
                    }
                ],
                "no_supplier_payout": True,
                "type": "COD_INSURANCE",
                "applied_stp_num": 10,
                "required_item_value": True,
                "service_id": "SGN-VAN-1000",
                "description_url": "https://ahamove.com/phi-khai-gia-cho-truck-ahmxsaladin/",
                "benefit_url": "https://ahamove.com/phi-khai-gia-cho-truck-ahmxsaladin/",
                "non_cod_description": "Bồi thường mất mát hoặc hư hỏng theo danh mục hàng hoá của bạn",
                "none_cod_price_blocks": {
                    "electronics": 2000,
                    "health & beauty": 2000,
                    "housing & lifestyle": 2000,
                    "food": 2000,
                    "mother & baby": 2000,
                    "fashion": 2000,
                    "grocery": 2000,
                    "restaurant": 2000,
                    "sport": 2000,
                    "drink": 2000,
                    "other": 2000,
                    "individual needs": 2000,
                    "transportation": 2000
                },
                "service_group_id": "VAN-1000"
            },
            {
                "_id": "SGN-VAN-1000-BOCXEP-KLLHC",
                "name": "Bốc xếp không lên lầu - 2 chiều",
                "enable": True,
                "name_vi_vn": "Bốc xếp không lên lầu - 2 chiều",
                "name_en_us": "2 Ways moving help (ground floor only)",
                "icon_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_loading_per_helper.png",
                "img_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_loading_per_helper.png",
                "order": 2,
                "price": 165000,
                "description_vi_vn": "Tài xế hỗ trợ bốc xếp hàng hóa (đã được đóng thùng) xuống xe đến địa điểm chỉ định trong vòng 100m VÀ ngược lại (Áp dụng cho 2 lượt và không lên lầu). Các trường hợp phát sinh thêm, vui lòng thoả thuận với tài xế.",
                "description_en_us": "Driver provides moving help (already packaged) from vehicle to designated location within 100m AND vice versa (Apply for 2 turns and ground floor only). For additional cases, please negotiate with the driver.",
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-VAN-1000",
                "category": "UNLOADING",
                "service_group_id": "VAN-1000",
                "group_id": "BOCXEP"
            },
            {
                "_id": "SGN-VAN-1000-LOADERS",
                "name": "Thêm người bốc xếp",
                "enable": True,
                "name_vi_vn": "Thêm người bốc xếp",
                "name_en_us": "Thêm người bốc xếp",
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/more-pickers.png",
                "img_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/more-pickers.png",
                "order": 2,
                "price": 300000,
                "max_input": 3,
                "description_vi_vn": "Hàng hoá số lượng lớn hay có kích thước cồng kềnh, nặng và yêu cầu phải có 2 người bưng trở lên",
                "no_commission": False,
                "description_en_us": "Hàng hoá số lượng lớn hay có kích thước cồng kềnh, nặng và yêu cầu phải có 2 người bưng trở lên",
                "type": "PER_UNIT",
                "description": "Hàng hoá số lượng lớn hay có kích thước cồng kềnh, nặng và yêu cầu phải có 2 người bưng trở lên",
                "service_id": "SGN-VAN-1000",
                "service_group_id": "VAN-1000",
                "group_id": "LOADER"
            },
            {
                "_id": "SGN-VAN-1000-BOCXEP-LLMC",
                "name": "Bốc xếp tại nhà có lầu - 1 chiều",
                "enable": True,
                "name_vi_vn": "Bốc xếp tại nhà có lầu - 1 chiều",
                "name_en_us": "1 Way moving help (Maximum 1 Floor)",
                "icon_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_moving_help_upstair.png",
                "img_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_moving_help_upstair.png",
                "order": 3,
                "price": 165000,
                "description_vi_vn": "Tài xế hỗ trợ bốc xếp hàng hóa (đã được đóng thùng) xuống xe đến địa điểm chỉ định trong vòng 100m HOẶC ngược lại (Áp dụng cho 1 lượt, 1 lầu). Các trường hợp phát sinh thêm, vui lòng thoả thuận với tài xế.",
                "description_en_us": "Driver provides moving help (already packaged) from vehicle to designated location within 100m OR vice versa (Apply for 1 turn and maximum 1 floor). For additional cases, please negotiate with the driver.",
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-VAN-1000",
                "category": "UNLOADING",
                "service_group_id": "VAN-1000",
                "group_id": "BOCXEP"
            },
            {
                "_id": "SGN-VAN-1000-BOCXEP-LLHC",
                "name": "Bốc xếp tại nhà có lầu - 2 chiều",
                "enable": True,
                "name_vi_vn": "Bốc xếp tại nhà có lầu - 2 chiều",
                "name_en_us": "2 Ways moving help (Maximum 1 Floor)",
                "icon_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_moving_help_upstair.png",
                "img_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_moving_help_upstair.png",
                "order": 4,
                "price": 240000,
                "description_vi_vn": "Tài xế hỗ trợ bốc xếp hàng hóa (đã được đóng thùng) xuống xe đến địa điểm chỉ định trong vòng 100m VÀ ngược lại (Áp dụng cho 2 lượt, 1 lầu). Các trường hợp phát sinh thêm, vui lòng thoả thuận với tài xế.",
                "description_en_us": "Driver provides moving help (already packaged) from vehicle to designated location within 100m AND vice versa (Apply for 1 turn and maximum 1 floor). For additional cases, please negotiate with the driver.",
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-VAN-1000",
                "category": "UNLOADING",
                "service_group_id": "VAN-1000",
                "group_id": "BOCXEP"
            },
            {
                "_id": "SGN-VAN-1000-ROUND-TRIP",
                "name": "Quay lại điểm lấy hàng",
                "enable": True,
                "name_vi_vn": "Quay lại điểm lấy hàng",
                "name_en_us": "Return to pick up location",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_round_trip.png",
                "img_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_round_trip.png",
                "order": 5,
                "description_vi_vn": "Tài xế sẽ quay lại điểm lấy hàng với cước phí bằng 50% phí khoảng cách. Lưu ý: Phí khoảng cách là cước phí dựa theo số km vận chuyển, không bao gồm phí điểm dừng và các loại phí khác.",
                "description_en_us": "Driver will return to pick up location for 50% of distance fee. Note: Distance fee is calculated solely by the travel distance, it does not include stop fee and others fee",
                "type": "COMMISSION_DISTANCE_PERCENTAGE",
                "price": 0.5,
                "description": "",
                "service_id": "SGN-VAN-1000",
                "service_group_id": "VAN-1000",
                "group_id": "ROUND-TRIP"
            }
        ],
        "currency": "VND"
    },
    {
        "_id": "SGN-TRUCK-1000",
        "enable": True,
        "order": 11,
        "city_id": "SGN",
        "name": "Xe tải 1000kg",
        "rebroadcast_interval": 1200,
        "rebroadcast_limit": 3,
        "name_vi_vn": "Xe tải 1000kg",
        "name_en_us": "Xe tải 1000kg",
        "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/services/truck/Truck-1000.png",
        "map_icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/services/Truck_service_map_icon/Truck.png",
        "parent_id": "",
        "stop_fee": 22000,
        "commission_type": "PERCENTAGE",
        "commission_value": 0.212,
        "distance_fee": "245000 if x <= 4 else 245000 + (x - 4) * 28500 if x <= 15 else 245000 + 11 * 28500 + (x - 15) * 24500",
        "vat_rate": 0.1,
        "broadcast_distance": 20000,
        "require_pod": True,
        "accept_interval": 1800,
        "require_to": True,
        "max_stop_points": 10,
        "description_en_us": "📦 (LxWxH) 3 x 1.6 x 1.7 meters",
        "description_vi_vn": "📦 (DxRxC) 3 x 1.6 x 1.7 mét",
        "fee_description_en_us": "Payload capacity: 1,000kg\nSuitable goods (LxWxH): 3 x 1.6 x 1.7 meters\n\nDistance fee:\n- From 00 - 04km: 245,000 VND\n- From 04 - 15km: 26,000 VND/km\n- Over 15km: 22,000 VND/km\n\nTruck ban hours (Urban areas)\n- From 06:00 - 09:00 AM\n- From 16:00 - 20:00 PM\n*Tip: Use VAN during truck ban hours to optimize orders\n\nMaximum COD: 10,000,000 VND\nCOD fee:\n- COD <   2,000,000 VND: Free\n- COD >= 2,000,000 VND: 0.8% x Value of COD",
        "fee_description_vi_vn": "Khối lượng chuyên chở: 1,000kg\nHàng hoá phù hợp (DxRxC): 3 x 1.6 x 1.7 mét\n\nPhí quãng đường:\n- Từ 00 - 04km: 245,000đ\n- Từ 04 - 15km: 26,000đ/km\n- Trên 15km: 22,000đ/km\n\nKhung giờ cấm tải (Nội thành)\n- Từ 06:00 - 09:00 AM\n- Từ 16:00 - 20:00 PM\n*Mách bạn: Hãy sử dụng xe tải VAN trong khung giờ cấm tải để tối ưu đơn hàng\n\nMức COD tối đa: 10,000,000đ\nPhí COD:\n- COD <   2,000,000đ: Miễn phí\n- COD >= 2,000,000đ: 0.8% x Giá trị COD",
        "cross_city": {
            "enable": True,
            "cities": [
                "SGN",
                "THD",
                "BHC"
            ]
        },
        "cross_service": {
            "enable": True,
            "services": [
                "SGN-TRICYCLE",
                "SGN-TRUCK-1000",
                "SGN-TRUCK-500",
                "SGN-VAN-500",
                "SGN-VAN-1000"
            ]
        },
        "timeout": 1800,
        "delivery_type": "TRUCK",
        "cod": 10000000,
        "max_cod": 1000000,
        "available_districts": [
            "VN.HC.BC",
            "VN.HC.CC",
            "VN.HC.CG",
            "VN.HC.HM",
            "VN.HC.NB",
            "VN.HC.BH",
            "VN.HC.BT",
            "VN.HC.GV",
            "VN.HC.PN",
            "VN.HC.QJ",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.QA",
            "VN.HC.QB",
            "VN.HC.QC",
            "VN.HC.QD",
            "VN.HC.QE",
            "VN.HC.QF",
            "VN.HC.QG",
            "VN.HC.QH",
            "VN.HC.QI"
        ],
        "advance_broadcast_distance": 15500,
        "payment_method": [
            {
                "description": "Cash",
                "description_vi_vn": "Tiền mặt",
                "payment": "cash",
                "order": 1
            },
            {
                "description": "Balance",
                "description_vi_vn": "Ví AhaMove",
                "payment": "balance",
                "order": 2
            },
            {
                "description": "MoMo e-Wallet",
                "description_vi_vn": "Ví điện tử MoMo",
                "payment": "momo",
                "order": 3
            },
            {
                "description": "ZaloPay e-Wallet",
                "description_vi_vn": "Ví điện tử ZaloPay",
                "payment": "Zalopay",
                "order": 4
            }
        ],
        "cod_commission": {
            "value": 0.008,
            "none_commission_limit": 2000000
        },
        "recommendation_config": {
            "supplier_timeout": 30,
            "recommend_timeout": 90,
            "recommend_radius": 3500,
            "sleep_interval": 90,
            "dispatch_mode": "RECOMMEND",
            "pool_mode": "NO_POOL",
            "pool_saving_threshold": 0.2,
            "poolable": False
        },
        "enable_platform": [
            "momo_deeplink",
            "momo_permission",
            "zalo",
            "zalopay",
            "smartpay_deeplink",
            "viettel-pay_deeplink",
            "onwheel"
        ],
        "advance_max_concurrent_orders": 1,
        "max_concurrent_orders": 1,
        "supplier_description": "Thực hiện trong 120 phút, nhận tối đa 1 đơn",
        "supplier_description_url": "https://ahamove.com/dich-vu-ba-gac-tai-tai-van/",
        "route_api_url": "http://ops-osrm-car.ops-tech:8080/route/v1/driving/",
        "enable_cancellation_punishment": False,
        "distance_fee_v3": {
            "blocks": [
                {
                    "from": 0,
                    "to": 4,
                    "base": 245000,
                    "price_multiplier": 0
                },
                {
                    "from": 4,
                    "to": 15,
                    "base": 245000,
                    "price_multiplier": 28500
                },
                {
                    "from": 15,
                    "to": 100000,
                    "base": 558500,
                    "price_multiplier": 24500
                }
            ],
            "hour_rates": []
        },
        "truck_ban": {
            "ban_districts": [
                {
                    "_id": 260,
                    "hasc_2": "VN.HC.BH",
                    "name_2": "Bình Thạnh",
                    "city_id": "SGN",
                    "name": "BH",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 26
                },
                {
                    "_id": 267,
                    "hasc_2": "VN.HC.PN",
                    "name_2": "Phú Nhuận",
                    "city_id": "SGN",
                    "name": "PN",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 29
                },
                {
                    "_id": 268,
                    "hasc_2": "VN.HC.QJ",
                    "name_2": "Quận 10",
                    "city_id": "SGN",
                    "name": "QJ",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 30
                },
                {
                    "_id": 269,
                    "hasc_2": "VN.HC.QK",
                    "name_2": "Quận 11",
                    "city_id": "SGN",
                    "name": "QK",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 31
                },
                {
                    "_id": 270,
                    "hasc_2": "VN.HC.QL",
                    "name_2": "Quận 12",
                    "city_id": "SGN",
                    "name": "QL",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 32
                },
                {
                    "_id": 271,
                    "hasc_2": "VN.HC.QA",
                    "name_2": "Quận 1",
                    "city_id": "SGN",
                    "name": "QA",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 33
                },
                {
                    "_id": 273,
                    "hasc_2": "VN.HC.QC",
                    "name_2": "Quận 3",
                    "city_id": "SGN",
                    "name": "QC",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 35
                },
                {
                    "_id": 274,
                    "hasc_2": "VN.HC.QD",
                    "name_2": "Quận 4",
                    "city_id": "SGN",
                    "name": "QD",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 36
                },
                {
                    "_id": 275,
                    "hasc_2": "VN.HC.QE",
                    "name_2": "Quận 5",
                    "city_id": "SGN",
                    "name": "QE",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 37
                },
                {
                    "_id": 276,
                    "hasc_2": "VN.HC.QF",
                    "name_2": "Quận 6",
                    "city_id": "SGN",
                    "name": "QF",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 38
                },
                {
                    "_id": 277,
                    "hasc_2": "VN.HC.QG",
                    "name_2": "Quận 7",
                    "city_id": "SGN",
                    "name": "QG",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 39
                },
                {
                    "_id": 278,
                    "hasc_2": "VN.HC.QH",
                    "name_2": "Quận 8",
                    "city_id": "SGN",
                    "name": "QH",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 40
                },
                {
                    "_id": 280,
                    "hasc_2": "VN.HC.TB",
                    "name_2": "Tân Bình",
                    "city_id": "SGN",
                    "name": "TB",
                    "tick": True,
                    "spc_nWrXb": 0,
                    "idx_nWrXb": 42
                }
            ],
            "recommend_service": "",
            "enable": True,
            "ban_hours": [
                {
                    "from": 14,
                    "to": 20
                },
                {
                    "from": 6,
                    "to": 12
                }
            ]
        },
        "is_tip_allowed": True,
        "priority_score": 6,
        "vehicle_info": {
            "image": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/services/truck/Truck-1000.png",
            "length": 3.0,
            "width": 1.6,
            "height": 1.7,
            "weight": 1000.0,
            "box_volume": 10.0,
            "description_vi_vn": "Miêu tả Truck 1000kg",
            "description_en_us": "Description Truck 1000kg",
            "short_intro_vi": "Thích hợp cho hàng hoá vừa và không hoạt động trong khung giờ cấm tải ",
            "short_intro_en": "This vehicle is suitable to carry medium parcels and deactive in truck ban hours",
            "short_description_vi": "3.0 x 1.6 x 1.7 mét. Lên tới 1000kg",
            "short_description_en": "3.0 x 1.6 x 1.7 Meter. Up to 1000kgs"
        },
        "group_id": "TRUCK-1000",
        "animated_url": "https://i.imgur.com/xiDxEYN.png",
        "requests": [
            {
                "_id": "SGN-TRUCK-1000-INSURANCE",
                "name": "Khai giá hàng hoá",
                "name_vi_vn": "Khai giá hàng hoá",
                "name_en_us": "Value declaration",
                "enable": True,
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/Insurance/secure+24x24%402x.png",
                "order": 1,
                "price_blocks": [
                    {
                        "from": 0,
                        "to": 10000001,
                        "price": 2000,
                        "description_vi_vn": "Bồi thường mất mát hoặc hư hỏng theo giá trị hàng hoá của bạn",
                        "description_en_us": "Coverage for loss or damage according to the value of your items"
                    }
                ],
                "no_supplier_payout": True,
                "type": "COD_INSURANCE",
                "applied_stp_num": 10,
                "required_item_value": True,
                "service_id": "SGN-TRUCK-1000",
                "description_url": "https://ahamove.com/phi-khai-gia-cho-truck-ahmxsaladin/",
                "benefit_url": "https://ahamove.com/phi-khai-gia-cho-truck-ahmxsaladin/",
                "non_cod_description": "Bồi thường mất mát hoặc hư hỏng theo danh mục hàng hoá của bạn",
                "none_cod_price_blocks": {
                    "electronics": 2000,
                    "health & beauty": 2000,
                    "housing & lifestyle": 2000,
                    "food": 2000,
                    "mother & baby": 2000,
                    "fashion": 2000,
                    "grocery": 2000,
                    "restaurant": 2000,
                    "sport": 2000,
                    "drink": 2000,
                    "other": 2000,
                    "individual needs": 2000,
                    "transportation": 2000
                },
                "service_group_id": "TRUCK-1000"
            },
            {
                "_id": "SGN-TRUCK-1000-TRANSFER-COD",
                "name": "Thu hộ qua ví điện tử (new)",
                "enable": True,
                "transfer_cod": True,
                "support_remarks": True,
                "name_vi_vn": "Thu hộ qua ví điện tử (new)",
                "name_en_us": "Collect payment via e-wallet (new)",
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/icon-POD-extraservice.png",
                "order": 1,
                "price": 0,
                "no_commission": True,
                "type": "BOOLEAN",
                "service_id": "SGN-TRUCK-1000",
                "img_url": "http://file.hstatic.net/1000010797/file/hand-to-hand.png",
                "description_vi_vn": "Tài xế không cần ứng trước tiền thu hộ. Người nhận chỉ cần quét mã QR để thanh toán qua ví điện tử hoặc ứng dụng Mobile Banking khi tài xế đến giao hàng. Tiền thu hộ sẽ tự động chuyển vào tài khoản COD của bạn sau khi đơn hàng hoàn tất.",
                "description_en_us": "Your driver doesn't have to pay in advance. Upon delivery, the recipient scans a QR code to pay via an e-wallet or Mobile Banking app. Payment will be transferred to your COD account once the order is complete.",
                "subtype": "epayment_on_delivery",
                "service_group_id": "TRUCK-1000"
            },
            {
                "_id": "SGN-TRUCK-1000-LOADERS",
                "name": "Thêm người bốc xếp",
                "enable": True,
                "name_vi_vn": "Thêm người bốc xếp",
                "name_en_us": "Thêm người bốc xếp",
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/more-pickers.png",
                "img_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/more-pickers.png",
                "order": 2,
                "price": 300000,
                "max_input": 3,
                "description_vi_vn": "Hàng hoá số lượng lớn hay có kích thước cồng kềnh, nặng và yêu cầu phải có 2 người bưng trở lên",
                "no_commission": False,
                "description_en_us": "Hàng hoá số lượng lớn hay có kích thước cồng kềnh, nặng và yêu cầu phải có 2 người bưng trở lên",
                "type": "PER_UNIT",
                "description": "Hàng hoá số lượng lớn hay có kích thước cồng kềnh, nặng và yêu cầu phải có 2 người bưng trở lên",
                "service_id": "SGN-TRUCK-1000",
                "service_group_id": "TRUCK-1000",
                "group_id": "LOADER"
            },
            {
                "_id": "SGN-TRUCK-1000-ROUND-TRIP",
                "name": "Quay lại điểm lấy hàng",
                "enable": True,
                "name_vi_vn": "Quay lại điểm lấy hàng",
                "name_en_us": "Return to pick up location",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_round_trip.png",
                "img_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_round_trip.png",
                "order": 3,
                "description_vi_vn": "Tài xế sẽ quay lại điểm lấy hàng với cước phí bằng 50% phí khoảng cách. Lưu ý: Phí khoảng cách là cước phí dựa theo số km vận chuyển, không bao gồm phí điểm dừng và các loại phí khác.",
                "description_en_us": "Driver will return to pick up location for 50% of distance fee. Note: Distance fee is calculated solely by the travel distance, it does not include stop fee and others fee",
                "type": "COMMISSION_DISTANCE_PERCENTAGE",
                "price": 0.5,
                "description": "",
                "service_id": "SGN-TRUCK-1000",
                "service_group_id": "TRUCK-1000",
                "group_id": "ROUND-TRIP"
            }
        ],
        "currency": "VND"
    },
    {
        "_id": "SGN-TRUCK-2000",
        "enable": True,
        "order": 11,
        "city_id": "SGN",
        "name": "Xe Tải 2000kg",
        "name_vi_vn": "Xe Tải 2000kg",
        "name_en_us": "Xe Tải 2000kg",
        "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/services/truck/Truck-2000.png",
        "map_icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/services/Truck_service_map_icon/Truck.png",
        "parent_id": "",
        "stop_fee": 44000,
        "commission_type": "PERCENTAGE",
        "commission_value": 0.212,
        "distance_fee": "(1.5 if 15.5<=h<=20 else 1)*(420000 if x <= 4 else 420000 + (x - 4) * 29500 if x <= 10 else 420000 + 6 * 29500 + (x - 10) * 29500 if x <= 15 else 420000 + 6 * 29500 + 5 * 29500  + (x - 15) * 25500)",
        "broadcast_distance": 5000,
        "require_pod": True,
        "accept_interval": 1800,
        "require_to": True,
        "max_stop_points": 10,
        "notify_package_return": True,
        "description_en_us": "📦 (LxWxH) 3.5 x 1.6 x 1.7 meters",
        "description_vi_vn": "📦 (DxRxC) 3.5 x 1.6 x 1.7 mét",
        "fee_description_en_us": "\"Payload capacity: 2,000kg\nSuitable goods (LxWxH): 3.5 x 1.6 x 1.7 meters\n\nDistance fee:\n- From 00 - 04km: 420,000 VND\n- From 04 - 15km: 29,500 VND/km\n- Over 15km: 25,500 VND/km\n\nStop-fee: 44,000 VND/stop\n\nTruck ban hours (Urban areas)\n- From 06:00 - 09:00 AM\n- From 16:00 - 19:00 PM (HN) / 20:00 PM (TP.HCM)\n*Tip: Use VAN during truck ban hours to optimize orders\n\nMaximum COD: 10,000,000 VND\nCOD fee:\n- COD <   2,000,000 VND: Free\n- COD >= 2,000,000 VND: 0.88% x Value of COD\"",
        "fee_description_vi_vn": "\"Khối lượng chuyên chở: 2,000kg\nHàng hoá phù hợp (DxRxC): 3.5 x 1.6 x 1.7 mét\n\nPhí quãng đường:\n- Từ 00 - 04km: 420,000đ\n- Từ 04 - 15km: 29,500đ/km\n- Trên 15km: 25,500đ/km\n\nPhí điểm dừng: 44,000đ/điểm dừng\n\nKhung giờ cấm tải (Nội thành)\n- Từ 06:00 - 09:00 AM\n- Từ 16:00 - 19:00 PM (HN) / 20:00 PM (TP.HCM)\n*Mách bạn: Hãy sử dụng xe tải VAN trong khung giờ cấm tải để tối ưu đơn hàng\n\nMức COD tối đa: 10,000,000đ\nPhí COD:\n- COD <   2,000,000đ: Miễn phí\n- COD >= 2,000,000đ: 0.88% x Giá trị COD\"",
        "cross_service": {
            "enable": False,
            "services": []
        },
        "cross_city": {
            "enable": True,
            "cities": [
                "SGN",
                "THD",
                "BHC"
            ]
        },
        "timeout": 1800,
        "cod": 10000000,
        "max_cod": 1000000,
        "delivery_type": "TRUCK",
        "available_districts": [
            "VN.HC.BC",
            "VN.HC.CC",
            "VN.HC.CG",
            "VN.HC.HM",
            "VN.HC.NB",
            "VN.HC.BH",
            "VN.HC.BT",
            "VN.HC.GV",
            "VN.HC.PN",
            "VN.HC.QJ",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.QA",
            "VN.HC.QB",
            "VN.HC.QC",
            "VN.HC.QD",
            "VN.HC.QE",
            "VN.HC.QF",
            "VN.HC.QG",
            "VN.HC.QH",
            "VN.HC.QI"
        ],
        "cod_commission": {
            "value": 0.0088,
            "none_commission_limit": 2000000
        },
        "advance_broadcast_distance": 7000,
        "payment_method": [
            {
                "description": "Cash",
                "description_vi_vn": "Tiền mặt",
                "payment": "cash",
                "order": 1
            },
            {
                "description": "Balance",
                "description_vi_vn": "Ví AhaMove",
                "payment": "balance",
                "order": 2
            },
            {
                "description": "MoMo e-Wallet",
                "description_vi_vn": "Ví điện tử MoMo",
                "payment": "momo",
                "order": 3
            },
            {
                "description": "ZaloPay e-Wallet",
                "description_vi_vn": "Ví điện tử ZaloPay",
                "payment": "Zalopay",
                "order": 4
            }
        ],
        "recommendation_config": {
            "supplier_timeout": 30,
            "recommend_timeout": 90,
            "recommend_radius": 5000,
            "sleep_interval": 90,
            "dispatch_mode": "RECOMMEND",
            "pool_mode": "NO_POOL",
            "pool_saving_threshold": 0.2,
            "poolable": False
        },
        "enable_platform": [
            "momo_deeplink",
            "momo_permission",
            "zalo",
            "zalopay",
            "smartpay_deeplink",
            "viettel-pay_deeplink",
            "onwheel"
        ],
        "advance_max_concurrent_orders": 1,
        "max_concurrent_orders": 1,
        "same_district_delivery": False,
        "same_district_delivery_areas": "",
        "supplier_description": "Thực hiện trong 120 phút, nhận tối đa 1 đơn",
        "supplier_description_url": "https://ahamove.com/dich-vu-ba-gac-tai-tai-van/",
        "enable_cancellation_punishment": False,
        "vat_rate": 0.1,
        "route_api_url": "http://ops-osrm-car.ops-tech:8080/route/v1/driving/",
        "tooltips": {
            "ASSIGNING": {
                "message": [
                    "Đơn hàng của bạn đã được AhaMove xác nhận.",
                    "Hệ thống đang tìm kiếm đối tác giao hàng.",
                    "Vui lòng chờ trong vòng 10 - 20 phút."
                ],
                "message_vi_vn": [
                    "Đơn hàng của bạn đã được AhaMove xác nhận.",
                    "Hệ thống đang tìm kiếm đối tác giao hàng.",
                    "Vui lòng chờ trong vòng 10 - 20 phút."
                ]
            },
            "ACCEPTED": {
                "message": [
                    "Xin chúc mừng! Đã có tài xế nhận đơn hàng của bạn.",
                    "Tài xế sẽ đến điểm lấy hàng trong vòng 15 - 60 phút.",
                    "Hãy liên hệ tài xế nếu bạn có bất kỳ thay đổi nào."
                ],
                "message_vi_vn": [
                    "Xin chúc mừng! Đã có tài xế nhận đơn hàng của bạn.",
                    "Tài xế sẽ đến điểm lấy hàng trong vòng 15 - 60 phút.",
                    "Hãy liên hệ tài xế nếu bạn có bất kỳ thay đổi nào."
                ]
            }
        },
        "rebroadcast_interval": 1200,
        "rebroadcast_limit": 3,
        "distance_fee_v3": {
            "blocks": [
                {
                    "from": 0,
                    "to": 4,
                    "base": 420000,
                    "price_multiplier": 0
                },
                {
                    "from": 4,
                    "to": 10,
                    "base": 420000,
                    "price_multiplier": 29500
                },
                {
                    "from": 10,
                    "to": 15,
                    "base": 597000,
                    "price_multiplier": 29500
                },
                {
                    "from": 15,
                    "to": 100000,
                    "base": 744500,
                    "price_multiplier": 25500
                }
            ],
            "hour_rates": [
                {
                    "from": 0,
                    "to": 15.5,
                    "rate": 1
                },
                {
                    "from": 15.5,
                    "to": 20,
                    "rate": 1.5
                }
            ]
        },
        "stop_failed": 0,
        "truck_ban": {
            "enable": True,
            "ban_hours": [
                {
                    "from": 6,
                    "to": 12
                },
                {
                    "from": 14,
                    "to": 20
                }
            ],
            "ban_districts": [
                {
                    "_id": 259,
                    "hasc_2": "VN.HC.BC",
                    "name_2": "Bình Chánh",
                    "city_id": "SGN",
                    "name": "BC",
                    "tick": True
                },
                {
                    "_id": 262,
                    "hasc_2": "VN.HC.CC",
                    "name_2": "Củ Chi",
                    "city_id": "SGN",
                    "name": "CC",
                    "tick": True
                }
            ]
        },
        "priority_score": 6,
        "vehicle_info": {
            "image": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/services/truck/Truck-2000.png",
            "length": 3.5,
            "width": 1.6,
            "height": 1.7,
            "weight": 2000,
            "short_intro_vi": "Thích hợp cho hàng hoá lớn và không hoạt động trong khung giờ cấm tải ",
            "short_intro_en": "This vehicle is suitable to carry big parcels and deactive in truck ban hours",
            "short_description_vi": "3.5 x 1.6 x 1.7 mét. Lên tới 2000kg",
            "short_description_en": "3.5 x 1.6 x 1.7 Meter. Up to 2000kgs",
            "box_volume": 10,
            "description_vi_vn": "\"Khối lượng chuyên chở: 2,000kg\nHàng hoá phù hợp (DxRxC): 3.5 x 1.6 x 1.7 mét\n\nPhí quãng đường:\n- Từ 00 - 04km: 420,000đ\n- Từ 04 - 15km: 29,500đ/km\n- Trên 15km: 25,500đ/km\n\nPhí điểm dừng: 44,000đ/điểm dừng\n\nKhung giờ cấm tải (Nội thành)\n- Từ 06:00 - 09:00 AM\n- Từ 16:00 - 19:00 PM (HN) / 20:00 PM (TP.HCM)\n*Mách bạn: Hãy sử dụng xe tải VAN trong khung giờ cấm tải để tối ưu đơn hàng\n\nMức COD tối đa: 10,000,000đ\nPhí COD:\n- COD <   2,000,000đ: Miễn phí\n- COD >= 2,000,000đ: 0.88% x Giá trị COD\"",
            "description_en_us": "\"Payload capacity: 2,000kg\nSuitable goods (LxWxH): 3.5 x 1.6 x 1.7 meters\n\nDistance fee:\n- From 00 - 04km: 420,000 VND\n- From 04 - 15km: 29,500 VND/km\n- Over 15km: 25,500 VND/km\n\nStop-fee: 44,000 VND/stop\n\nTruck ban hours (Urban areas)\n- From 06:00 - 09:00 AM\n- From 16:00 - 19:00 PM (HN) / 20:00 PM (TP.HCM)\n*Tip: Use VAN during truck ban hours to optimize orders\n\nMaximum COD: 10,000,000 VND\nCOD fee:\n- COD <   2,000,000 VND: Free\n- COD >= 2,000,000 VND: 0.88% x Value of COD\""
        },
        "group_id": "TRUCK-2000",
        "animated_url": "https://i.imgur.com/xiDxEYN.png",
        "requests": [
            {
                "_id": "SGN-TRUCK-2000-INSURANCE",
                "name": "Khai giá hàng hoá",
                "name_vi_vn": "Khai giá hàng hoá",
                "name_en_us": "Value declaration",
                "enable": True,
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/Insurance/secure+24x24%402x.png",
                "order": 1,
                "price_blocks": [
                    {
                        "from": 0,
                        "to": 10000001,
                        "price": 2000,
                        "description_vi_vn": "Bồi thường mất mát hoặc hư hỏng theo giá trị hàng hoá của bạn",
                        "description_en_us": "Coverage for loss or damage according to the value of your items"
                    }
                ],
                "no_supplier_payout": True,
                "type": "COD_INSURANCE",
                "applied_stp_num": 10,
                "required_item_value": True,
                "service_id": "SGN-TRUCK-2000",
                "description_url": "https://ahamove.com/phi-khai-gia-cho-truck-ahmxsaladin/",
                "benefit_url": "https://ahamove.com/phi-khai-gia-cho-truck-ahmxsaladin/",
                "non_cod_description": "Bồi thường mất mát hoặc hư hỏng theo danh mục hàng hoá của bạn",
                "none_cod_price_blocks": {
                    "electronics": 2000,
                    "health & beauty": 2000,
                    "housing & lifestyle": 2000,
                    "food": 2000,
                    "mother & baby": 2000,
                    "fashion": 2000,
                    "grocery": 2000,
                    "restaurant": 2000,
                    "sport": 2000,
                    "drink": 2000,
                    "other": 2000,
                    "individual needs": 2000,
                    "transportation": 2000
                },
                "service_group_id": "TRUCK-2000"
            },
            {
                "_id": "SGN-TRUCK-2000-BOCXEP-KLLMC",
                "name": "Bốc xếp không lên lầu - 1 chiều",
                "name_en_us": "1 Way moving help (ground floor only)",
                "name_vi_vn": "Bốc xếp không lên lầu - 1 chiều",
                "icon_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_loading_per_helper.png",
                "order": 1,
                "price": 165000,
                "description_vi_vn": "Tài xế hỗ trợ bốc xếp hàng hóa (đã được đóng thùng) xuống xe đến địa điểm chỉ định trong vòng 100m HOẶC ngược lại (Áp dụng cho 1 lượt và không lên lầu). Các trường hợp phát sinh thêm, vui lòng thoả thuận với tài xế.",
                "description_en_us": "Driver provides moving help (already packaged) from vehicle to designated location within 100m OR vice versa (Apply for 1 turn and ground floor only). For additional cases, please negotiate with the driver.",
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-TRUCK-2000",
                "img_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_loading_per_helper.png",
                "enable": True,
                "service_group_id": "TRUCK-2000",
                "group_id": "BOCXEP"
            },
            {
                "_id": "SGN-TRUCK-2000-CHUYENNHA",
                "name": "Gói hỗ trợ chuyển nhà cơ bản",
                "name_vi_vn": "Gói hỗ trợ chuyển nhà cơ bản",
                "name_en_us": "Gói hỗ trợ chuyển nhà cơ bản",
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/house-moving.png",
                "order": 1,
                "price": 800000,
                "description_vi_vn": "Chi tiết gói: \n- Thêm 1 người bốc xếp: 350000 \n- Hỗ trợ bốc xếp: 330000\n- Phí chờ 2h: 120000\n \nLưu ý: \n- Địa hình vận chuyển: Không quá 100m và 2 tầng/ lầu tại 2 chiều.\n- Vui lòng tháo lắp đồ điện lạnh, nội thất và đóng gói hàng hoá trước khi đặt dịch vụ\n- Trường hợp có phát sinh cước luân chuyển, bốc xếp vui lòng liên hệ tổng đài 1900545411 để được xác nhận.",
                "description_en_us": "Chi tiết gói: \n- Thêm 1 người bốc xếp: 350000 \n- Hỗ trợ bốc xếp: 330000\n- Phí chờ 2h: 120000\n \nLưu ý: \n- Địa hình vận chuyển: Không quá 100m và 2 tầng/ lầu tại 2 chiều.\n- Vui lòng tháo lắp đồ điện lạnh, nội thất và đóng gói hàng hoá trước khi đặt dịch vụ\n- Trường hợp có phát sinh cước luân chuyển, bốc xếp vui lòng liên hệ tổng đài 1900545411 để được xác nhận.",
                "type": "BOOLEAN",
                "description": "Chi tiết gói: \n- Thêm 1 người bốc xếp: 350000 \n- Hỗ trợ bốc xếp: 330000\n- Phí chờ 2h: 120000\n \nLưu ý: \n- Địa hình vận chuyển: Không quá 100m và 2 tầng/ lầu tại 2 chiều.\n- Vui lòng tháo lắp đồ điện lạnh, nội thất và đóng gói hàng hoá trước khi đặt dịch vụ\n- Trường hợp có phát sinh cước luân chuyển, bốc xếp vui lòng liên hệ tổng đài 1900545411 để được xác nhận.",
                "service_id": "SGN-TRUCK-2000",
                "img_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/house-moving.png",
                "enable": True,
                "options": [
                    {
                        "code": "ITEM_1",
                        "name_vi_vn": "Hỗ trợ bốc xếp (x2)",
                        "name_en_us": "Hỗ trợ bốc xếp (x2)",
                        "selectable": True
                    },
                    {
                        "code": "ITEM_2",
                        "name_vi_vn": "Phí chờ",
                        "name_en_us": "Phí chờ",
                        "selectable": True
                    },
                    {
                        "code": "ITEM_3",
                        "name_vi_vn": "Combo Bốc xếp và phí chờ",
                        "name_en_us": "Combo Bốc xếp và phí chờ",
                        "selectable": True
                    }
                ],
                "service_group_id": "TRUCK-2000",
                "group_id": "CHUYENNHA"
            },
            {
                "_id": "SGN-TRUCK-2000-BOCXEP-KLLHC",
                "name": "Bốc xếp không lên lầu - 2 chiều",
                "name_vi_vn": "Bốc xếp không lên lầu - 2 chiều",
                "name_en_us": "2 Ways moving help (ground floor only)",
                "icon_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_loading_per_helper.png",
                "order": 2,
                "price": 240000,
                "description_vi_vn": "Tài xế hỗ trợ bốc xếp hàng hóa (đã được đóng thùng) xuống xe đến địa điểm chỉ định trong vòng 100m VÀ ngược lại (Áp dụng cho 2 lượt và không lên lầu). Các trường hợp phát sinh thêm, vui lòng thoả thuận với tài xế.",
                "description_en_us": "Driver provides moving help (already packaged) from vehicle to designated location within 100m AND vice versa (Apply for 2 turns and ground floor only). For additional cases, please negotiate with the driver.",
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-TRUCK-2000",
                "img_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_loading_per_helper.png",
                "enable": True,
                "service_group_id": "TRUCK-2000",
                "group_id": "BOCXEP"
            },
            {
                "_id": "SGN-TRUCK-2000-LOADERS",
                "name": "Thêm người bốc xếp",
                "enable": True,
                "name_vi_vn": "Thêm người bốc xếp",
                "name_en_us": "Thêm người bốc xếp",
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/more-pickers.png",
                "img_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/more-pickers.png",
                "order": 2,
                "price": 350000,
                "max_input": 3,
                "description_vi_vn": "Hàng hoá số lượng lớn hay có kích thước cồng kềnh, nặng và yêu cầu phải có 2 người bưng trở lên",
                "no_commission": False,
                "description_en_us": "Hàng hoá số lượng lớn hay có kích thước cồng kềnh, nặng và yêu cầu phải có 2 người bưng trở lên",
                "type": "PER_UNIT",
                "description": "Hàng hoá số lượng lớn hay có kích thước cồng kềnh, nặng và yêu cầu phải có 2 người bưng trở lên",
                "service_id": "SGN-TRUCK-2000",
                "service_group_id": "TRUCK-2000",
                "group_id": "LOADER"
            },
            {
                "_id": "SGN-TRUCK-2000-BOCXEP-LLMC",
                "name": "Bốc xếp tại nhà 1 tầng/lầu - 1 chiều",
                "name_vi_vn": "Bốc xếp tại nhà 1 tầng/lầu - 1 chiều",
                "name_en_us": "1 Way moving help (Maximum 1 Floor)",
                "icon_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_moving_help_upstair.png",
                "order": 3,
                "price": 220000,
                "description_vi_vn": "Tài xế hỗ trợ bốc xếp hàng hóa (đã được đóng thùng) xuống xe đến địa điểm chỉ định trong vòng 100m HOẶC ngược lại (Áp dụng cho 1 lượt, 1 lầu). Các trường hợp phát sinh thêm, vui lòng thoả thuận với tài xế.",
                "description_en_us": "Driver provides moving help (already packaged) from vehicle to designated location within 100m OR vice versa (Apply for 1 turn and maximum 1 floor). For additional cases, please negotiate with the driver.",
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-TRUCK-2000",
                "img_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_moving_help_upstair.png",
                "enable": True,
                "service_group_id": "TRUCK-2000",
                "group_id": "BOCXEP"
            },
            {
                "_id": "SGN-TRUCK-2000-BOCXEP-LLHC",
                "name": "Bốc xếp tại nhà 1 tầng/lầu - 2 chiều",
                "enable": True,
                "name_vi_vn": "Bốc xếp tại nhà 1 tầng/lầu - 2 chiều",
                "name_en_us": "2 Ways moving help (ground floor only)",
                "icon_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_loading_per_helper.png",
                "img_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_loading_per_helper.png",
                "order": 4,
                "price": 330000,
                "description_vi_vn": "Tài xế hỗ trợ bốc xếp hàng hóa (đã được đóng thùng) xuống xe đến địa điểm chỉ định trong vòng 100m VÀ ngược lại (Áp dụng cho 2 lượt và không lên lầu). Các trường hợp phát sinh thêm, vui lòng thoả thuận với tài xế.",
                "description_en_us": "Driver provides moving help (already packaged) from vehicle to designated location within 100m AND vice versa (Apply for 2 turns and ground floor only). For additional cases, please negotiate with the driver.",
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-TRUCK-2000",
                "service_group_id": "TRUCK-2000",
                "group_id": "BOCXEP"
            },
            {
                "_id": "SGN-TRUCK-2000-ROUND-TRIP",
                "name": "Quay lại điểm lấy hàng",
                "name_vi_vn": "Quay lại điểm lấy hàng",
                "name_en_us": "Return to pick up location",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_round_trip.png",
                "img_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_round_trip.png",
                "order": 5,
                "description_vi_vn": "Tài xế sẽ quay lại điểm lấy hàng với cước phí bằng 50% phí khoảng cách. Lưu ý: Phí khoảng cách là cước phí dựa theo số km vận chuyển, không bao gồm phí điểm dừng và các loại phí khác.",
                "description_en_us": "Driver will return to pick up location for 50% of distance fee. Note: Distance fee is calculated solely by the travel distance, it does not include stop fee and others fee",
                "type": "COMMISSION_DISTANCE_PERCENTAGE",
                "price": 0.5,
                "description": "",
                "enable": True,
                "service_id": "SGN-TRUCK-2000",
                "supplier_description_vi_vn": "Đối tác tiến hành quay trở lại điểm lấy hàng sau khi giao thành công ",
                "supplier_description": "Đối tác tiến hành quay trở lại điểm lấy hàng sau khi giao thành công ",
                "supplier_description_url": "https://ahamove.com/dichvukemtheo",
                "service_group_id": "TRUCK-2000",
                "group_id": "ROUND-TRIP"
            },
            {
                "_id": "SGN-TRUCK-2000-PHICHO",
                "name": "Phí chờ (60,000 VNĐ/giờ)",
                "name_vi_vn": "Phí chờ (60,000 VNĐ/giờ)",
                "enable": True,
                "name_en_us": "Waiting fee (60,000 VND/hour)",
                "icon_url": "https://ahamove.com/wp-content/uploads/2022/01/waiting.png",
                "img_url": "https://ahamove.com/wp-content/uploads/2022/01/waiting.png",
                "order": 6,
                "price": 60000,
                "no_commission": True,
                "description_vi_vn": "Vui lòng chọn phụ phí thời gian chờ tương ứng để khích lệ tài xế trong trường hợp khách hàng có mong muốn tài xế chờ lâu hơn 45 phút kể từ thời điểm tài xế đến nơi lấy hàng.",
                "description_en_us": "In case customers want the driver to wait longer than 45 minutes from the time driver arrived, please choose the corresponding waiting fee to encourage the driver.",
                "max_input": 5,
                "type": "PER_UNIT",
                "description": "",
                "service_id": "SGN-TRUCK-2000",
                "service_group_id": "TRUCK-2000",
                "group_id": "PHICHO"
            },
            {
                "_id": "SGN-TRUCK-2000-TIP",
                "name": "Hỗ trợ tài xế",
                "enable": True,
                "name_vi_vn": "Hỗ trợ tài xế",
                "name_en_us": "Tipping",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/sr_tipping.png",
                "img_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/sr_tipping.png",
                "order": 12,
                "price": 10000,
                "max_input": 10,
                "description_vi_vn": "Hãy chọn dịch vụ này nếu bạn muốn hỗ trợ tài xế trong giờ cao điểm, khi thời tiết khó khăn, hoặc đơn giản là muốn thưởng thêm cho tài xế. Ngoài ra, tính năng này sẽ giúp cho đơn hàng của bạn được ưu tiên hơn trong thời gian cao điểm.",
                "no_commission": True,
                "description_en_us": "This will show your support or compliment to the driver, especially in rush hours, bad weather. Also, this feature will prioritize your request in peak time.",
                "type": "PER_UNIT",
                "description": "",
                "service_id": "SGN-TRUCK-2000",
                "service_group_id": "TRUCK-2000",
                "group_id": "TIP"
            }
        ],
        "currency": "VND"
    },
    {
        "_id": "SGN-TRUCK-1500",
        "enable": True,
        "order": 11,
        "city_id": "SGN",
        "name": "Xe Tải 1500kg",
        "name_vi_vn": "Xe Tải 1500kg",
        "name_en_us": "Xe Tải 1500kg",
        "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/services/truck/Truck-1500.png",
        "map_icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/services/Truck_service_map_icon/Truck.png",
        "parent_id": "",
        "stop_fee": 33000,
        "commission_type": "PERCENTAGE",
        "commission_value": 0.212,
        "distance_fee": "320000 if x <= 4 else 320000 + (x - 4) * 29000 if x <= 10 else 320000 + 6 * 29000 + (x - 10) * 29000 if x <= 15 else 320000 + 6 * 29000 + 5 * 29000  + (x - 15) * 25000",
        "broadcast_distance": 3500,
        "accept_interval": 1800,
        "require_to": True,
        "max_stop_points": 10,
        "notify_package_return": True,
        "description_en_us": "📦 (LxWxH) 3.2 x 1.6 x 1.7 meters",
        "description_vi_vn": "📦 (DxRxC) 3.2 x 1.6 x 1.7 mét",
        "fee_description_en_us": "\"Payload capacity: 1,500kg\nSuitable goods (LxWxH): 3.2 x 1.6 x 1.7 meters\n\nDistance fee:\n- From 00 - 04km: 320,000 VND\n- From 04 - 15km: 29,000 VND/km\n- Over 15km: 25,000 VND/km\n\nStop-fee: 33,000 VND/stop\n\nTruck ban hours (Urban areas)\n- From 06:00 - 09:00 AM\n- From 16:00 - 19:00 PM (HN) / 20:00 PM (TP.HCM)\n*Tip: Use VAN during truck ban hours to optimize orders\n\nMaximum COD: 10,000,000 VND\nCOD fee:\n- COD <   2,000,000 VND: Free\n- COD >= 2,000,000 VND: 0.88% x Value of COD\"",
        "fee_description_vi_vn": "\"Khối lượng chuyên chở: 1,500kg\nHàng hoá phù hợp (DxRxC): 3.2 x 1.6 x 1.7 mét\n\nPhí quãng đường:\n- Từ 00 - 04km: 320,000đ\n- Từ 04 - 15km: 29,000đ/km\n- Trên 15km: 25,000đ/km\n\nPhí điểm dừng: 33,000đ/điểm dừng\n\nKhung giờ cấm tải (Nội thành)\n- Từ 06:00 - 09:00 AM\n- Từ 16:00 - 19:00 PM (HN) / 20:00 PM (TP.HCM)\n*Mách bạn: Hãy sử dụng xe tải VAN trong khung giờ cấm tải để tối ưu đơn hàng\n\nMức COD tối đa: 10,000,000đ\nPhí COD:\n- COD <   2,000,000đ: Miễn phí\n- COD >= 2,000,000đ: 0.88% x Giá trị COD\"",
        "cross_service": {
            "enable": False,
            "services": []
        },
        "cross_city": {
            "enable": True,
            "cities": [
                "SGN",
                "THD",
                "BHC"
            ]
        },
        "timeout": 1800,
        "cod": 10000000,
        "max_cod": 10000000,
        "delivery_type": "TRUCK",
        "available_districts": [
            "VN.HC.BC",
            "VN.HC.CC",
            "VN.HC.CG",
            "VN.HC.HM",
            "VN.HC.NB",
            "VN.TDM",
            "VN.BH",
            "VN.LT",
            "VN.TA",
            "VN.DA",
            "VN.NT",
            "VN.TB",
            "VN.HC.BH",
            "VN.HC.BT",
            "VN.HC.GV",
            "VN.HC.PN",
            "VN.HC.QJ",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.QA",
            "VN.HC.QC",
            "VN.HC.QD",
            "VN.HC.QE",
            "VN.HC.QF",
            "VN.HC.QG",
            "VN.HC.QH",
            "VN.HC.TB",
            "VN.HC.TP",
            "VN.HC.TD"
        ],
        "cod_commission": {
            "value": 0.0088,
            "none_commission_limit": 2000000
        },
        "advance_broadcast_distance": 5500,
        "payment_method": [
            {
                "description": "Cash",
                "description_vi_vn": "Tiền mặt",
                "payment": "cash",
                "order": 1
            },
            {
                "description": "Balance",
                "description_vi_vn": "Ví AhaMove",
                "payment": "balance",
                "order": 2
            },
            {
                "description": "MoMo e-Wallet",
                "description_vi_vn": "Ví điện tử MoMo",
                "payment": "momo",
                "order": 3
            },
            {
                "description": "ZaloPay e-Wallet",
                "description_vi_vn": "Ví điện tử ZaloPay",
                "payment": "Zalopay",
                "order": 4
            }
        ],
        "recommendation_config": {
            "supplier_timeout": 30,
            "recommend_timeout": 90,
            "recommend_radius": 3500,
            "sleep_interval": 90,
            "dispatch_mode": "RECOMMEND",
            "pool_mode": "NO_POOL",
            "pool_saving_threshold": 0.2,
            "poolable": False
        },
        "enable_platform": [
            "momo_deeplink",
            "momo_permission",
            "zalo",
            "zalopay",
            "smartpay_deeplink",
            "viettel-pay_deeplink",
            "onwheel"
        ],
        "advance_max_concurrent_orders": 1,
        "max_concurrent_orders": 1,
        "same_district_delivery": False,
        "same_district_delivery_areas": "",
        "supplier_description": "Thực hiện trong 120 phút, nhận tối đa 1 đơn",
        "supplier_description_url": "https://ahamove.com/dich-vu-ba-gac-tai-tai-van/",
        "enable_cancellation_punishment": False,
        "vat_rate": 0.1,
        "route_api_url": "https://ep.ahamove.com/osrm-proxy/car/route/v1/driving/",
        "tooltips": {
            "ASSIGNING": {
                "message": [
                    "Đơn hàng của bạn đã được AhaMove xác nhận.",
                    "Hệ thống đang tìm kiếm đối tác giao hàng.",
                    "Vui lòng chờ trong vòng 10 - 20 phút."
                ],
                "message_vi_vn": [
                    "Đơn hàng của bạn đã được AhaMove xác nhận.",
                    "Hệ thống đang tìm kiếm đối tác giao hàng.",
                    "Vui lòng chờ trong vòng 10 - 20 phút."
                ]
            },
            "ACCEPTED": {
                "message": [
                    "Xin chúc mừng! Đã có tài xế nhận đơn hàng của bạn.",
                    "Tài xế sẽ đến điểm lấy hàng trong vòng 15 - 60 phút.",
                    "Hãy liên hệ tài xế nếu bạn có bất kỳ thay đổi nào."
                ],
                "message_vi_vn": [
                    "Xin chúc mừng! Đã có tài xế nhận đơn hàng của bạn.",
                    "Tài xế sẽ đến điểm lấy hàng trong vòng 15 - 60 phút.",
                    "Hãy liên hệ tài xế nếu bạn có bất kỳ thay đổi nào."
                ]
            }
        },
        "rebroadcast_interval": 1200,
        "rebroadcast_limit": 3,
        "distance_fee_v3": {
            "blocks": [
                {
                    "from": 0,
                    "to": 4,
                    "base": 320000,
                    "price_multiplier": 0
                },
                {
                    "from": 4,
                    "to": 10,
                    "base": 320000,
                    "price_multiplier": 29000
                },
                {
                    "from": 10,
                    "to": 15,
                    "base": 494000,
                    "price_multiplier": 29000
                },
                {
                    "from": 15,
                    "to": 100000,
                    "base": 639000,
                    "price_multiplier": 25000
                }
            ],
            "hour_rates": []
        },
        "truck_ban": {
            "ban_districts": [
                {
                    "_id": 260,
                    "hasc_2": "VN.HC.BH",
                    "name_2": "Bình Thạnh",
                    "city_id": "SGN",
                    "name": "BH",
                    "tick": True,
                    "spc_QdxLm": 0,
                    "idx_QdxLm": 26
                },
                {
                    "_id": 267,
                    "hasc_2": "VN.HC.PN",
                    "name_2": "Phú Nhuận",
                    "city_id": "SGN",
                    "name": "PN",
                    "tick": True,
                    "spc_QdxLm": 0,
                    "idx_QdxLm": 29
                },
                {
                    "_id": 268,
                    "hasc_2": "VN.HC.QJ",
                    "name_2": "Quận 10",
                    "city_id": "SGN",
                    "name": "QJ",
                    "tick": True,
                    "spc_QdxLm": 0,
                    "idx_QdxLm": 30
                },
                {
                    "_id": 269,
                    "hasc_2": "VN.HC.QK",
                    "name_2": "Quận 11",
                    "city_id": "SGN",
                    "name": "QK",
                    "tick": True,
                    "spc_QdxLm": 0,
                    "idx_QdxLm": 31
                },
                {
                    "_id": 271,
                    "hasc_2": "VN.HC.QA",
                    "name_2": "Quận 1",
                    "city_id": "SGN",
                    "name": "QA",
                    "tick": True,
                    "spc_QdxLm": 0,
                    "idx_QdxLm": 33
                },
                {
                    "_id": 273,
                    "hasc_2": "VN.HC.QC",
                    "name_2": "Quận 3",
                    "city_id": "SGN",
                    "name": "QC",
                    "tick": True,
                    "spc_QdxLm": 0,
                    "idx_QdxLm": 35
                },
                {
                    "_id": 274,
                    "hasc_2": "VN.HC.QD",
                    "name_2": "Quận 4",
                    "city_id": "SGN",
                    "name": "QD",
                    "tick": True,
                    "spc_QdxLm": 0,
                    "idx_QdxLm": 36
                },
                {
                    "_id": 275,
                    "hasc_2": "VN.HC.QE",
                    "name_2": "Quận 5",
                    "city_id": "SGN",
                    "name": "QE",
                    "tick": True,
                    "spc_QdxLm": 0,
                    "idx_QdxLm": 37
                },
                {
                    "_id": 276,
                    "hasc_2": "VN.HC.QF",
                    "name_2": "Quận 6",
                    "city_id": "SGN",
                    "name": "QF",
                    "tick": True,
                    "spc_QdxLm": 0,
                    "idx_QdxLm": 38
                },
                {
                    "_id": 277,
                    "hasc_2": "VN.HC.QG",
                    "name_2": "Quận 7",
                    "city_id": "SGN",
                    "name": "QG",
                    "tick": True,
                    "spc_QdxLm": 0,
                    "idx_QdxLm": 39
                },
                {
                    "_id": 278,
                    "hasc_2": "VN.HC.QH",
                    "name_2": "Quận 8",
                    "city_id": "SGN",
                    "name": "QH",
                    "tick": True,
                    "spc_QdxLm": 0,
                    "idx_QdxLm": 40
                },
                {
                    "_id": 280,
                    "hasc_2": "VN.HC.TB",
                    "name_2": "Tân Bình",
                    "city_id": "SGN",
                    "name": "TB",
                    "tick": True,
                    "spc_QdxLm": 0,
                    "idx_QdxLm": 42
                },
                {
                    "_id": 281,
                    "hasc_2": "VN.HC.TP",
                    "name_2": "Tân Phú",
                    "city_id": "SGN",
                    "name": "TP",
                    "tick": True,
                    "spc_QdxLm": 0,
                    "idx_QdxLm": 43
                }
            ],
            "enable": True,
            "ban_hours": [
                {
                    "from": 6,
                    "to": 17
                }
            ]
        },
        "priority_score": 6,
        "max_distance": 150000,
        "vehicle_info": {
            "image": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/services/truck/Truck-1500.png",
            "length": 3.2,
            "width": 1.6,
            "height": 1.7,
            "weight": 100.0,
            "box_volume": 10.0,
            "short_intro_vi": "Thích hợp cho hàng hoá lớn và không hoạt động trong khung giờ cấm tải ",
            "short_intro_en": "This vehicle is suitable to carry big parcels and deactive in truck ban hours",
            "short_description_vi": "3.2 x 1.6 x 1.7 mét. Lên tới 1500kg",
            "short_description_en": "3.2 x 1.6 x 1.7 Meter. Up to 1500kgs",
            "description_vi_vn": "\"Khối lượng chuyên chở: 1,500kg\nHàng hoá phù hợp (DxRxC): 3.2 x 1.6 x 1.7 mét\n\nPhí quãng đường:\n- Từ 00 - 04km: 320,000đ\n- Từ 04 - 15km: 29,000đ/km\n- Trên 15km: 25,000đ/km\n\nPhí điểm dừng: 33,000đ/điểm dừng\n\nKhung giờ cấm tải (Nội thành)\n- Từ 06:00 - 09:00 AM\n- Từ 16:00 - 19:00 PM (HN) / 20:00 PM (TP.HCM)\n*Mách bạn: Hãy sử dụng xe tải VAN trong khung giờ cấm tải để tối ưu đơn hàng\n\nMức COD tối đa: 10,000,000đ\nPhí COD:\n- COD <   2,000,000đ: Miễn phí\n- COD >= 2,000,000đ: 0.88% x Giá trị COD\"",
            "description_en_us": "\"Payload capacity: 1,500kg\nSuitable goods (LxWxH): 3.2 x 1.6 x 1.7 meters\n\nDistance fee:\n- From 00 - 04km: 320,000 VND\n- From 04 - 15km: 29,000 VND/km\n- Over 15km: 25,000 VND/km\n\nStop-fee: 33,000 VND/stop\n\nTruck ban hours (Urban areas)\n- From 06:00 - 09:00 AM\n- From 16:00 - 19:00 PM (HN) / 20:00 PM (TP.HCM)\n*Tip: Use VAN during truck ban hours to optimize orders\n\nMaximum COD: 10,000,000 VND\nCOD fee:\n- COD <   2,000,000 VND: Free\n- COD >= 2,000,000 VND: 0.88% x Value of COD\""
        },
        "group_id": "TRUCK-1500",
        "animated_url": "https://i.imgur.com/xiDxEYN.png",
        "requests": [
            {
                "_id": "SGN-TRUCK-1500-BOCXEP-KLLMC",
                "name": "Bốc xếp không lên lầu - 1 chiều",
                "name_en_us": "1 Way moving help (ground floor only)",
                "name_vi_vn": "Bốc xếp không lên lầu - 1 chiều",
                "icon_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_loading_per_helper.png",
                "order": 1,
                "price": 110000,
                "description_vi_vn": "Tài xế hỗ trợ bốc xếp hàng hóa (đã được đóng thùng) xuống xe đến địa điểm chỉ định trong vòng 100m HOẶC ngược lại (Áp dụng cho 1 lượt và không lên lầu). Các trường hợp phát sinh thêm, vui lòng thoả thuận với tài xế.",
                "description_en_us": "Driver provides moving help (already packaged) from vehicle to designated location within 100m OR vice versa (Apply for 1 turn and ground floor only). For additional cases, please negotiate with the driver.",
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-TRUCK-1500",
                "img_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_loading_per_helper.png",
                "enable": True,
                "service_group_id": "TRUCK-1500",
                "group_id": "BOCXEP"
            },
            {
                "_id": "SGN-TRUCK-1500-CHUYENNHA",
                "name": "Gói hỗ trợ chuyển nhà cơ bản",
                "name_vi_vn": "Gói hỗ trợ chuyển nhà cơ bản",
                "name_en_us": "Gói hỗ trợ chuyển nhà cơ bản",
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/house-moving.png",
                "order": 1,
                "price": 800000,
                "description_vi_vn": "Chi tiết gói: \n- Thêm 1 người bốc xếp: 350000 \n- Hỗ trợ bốc xếp: 330000\n- Phí chờ 2h: 120000\n \nLưu ý: \n- Địa hình vận chuyển: Không quá 100m và 2 tầng/ lầu tại 2 chiều.\n- Vui lòng tháo lắp đồ điện lạnh, nội thất và đóng gói hàng hoá trước khi đặt dịch vụ\n- Trường hợp có phát sinh cước luân chuyển, bốc xếp vui lòng liên hệ tổng đài 1900545411 để được xác nhận.",
                "description_en_us": "Chi tiết gói: \n- Thêm 1 người bốc xếp: 350000 \n- Hỗ trợ bốc xếp: 330000\n- Phí chờ 2h: 120000\n \nLưu ý: \n- Địa hình vận chuyển: Không quá 100m và 2 tầng/ lầu tại 2 chiều.\n- Vui lòng tháo lắp đồ điện lạnh, nội thất và đóng gói hàng hoá trước khi đặt dịch vụ\n- Trường hợp có phát sinh cước luân chuyển, bốc xếp vui lòng liên hệ tổng đài 1900545411 để được xác nhận.",
                "type": "BOOLEAN",
                "description": "Chi tiết gói: \n- Thêm 1 người bốc xếp: 350000 \n- Hỗ trợ bốc xếp: 330000\n- Phí chờ 2h: 120000\n \nLưu ý: \n- Địa hình vận chuyển: Không quá 100m và 2 tầng/ lầu tại 2 chiều.\n- Vui lòng tháo lắp đồ điện lạnh, nội thất và đóng gói hàng hoá trước khi đặt dịch vụ\n- Trường hợp có phát sinh cước luân chuyển, bốc xếp vui lòng liên hệ tổng đài 1900545411 để được xác nhận.",
                "service_id": "SGN-TRUCK-1500",
                "img_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/house-moving.png",
                "enable": True,
                "options": [
                    {
                        "code": "ITEM_1",
                        "name_vi_vn": "Hỗ trợ bốc xếp (x2)",
                        "name_en_us": "Hỗ trợ bốc xếp (x2)",
                        "selectable": True
                    },
                    {
                        "code": "ITEM_2",
                        "name_vi_vn": "Phí chờ",
                        "name_en_us": "Phí chờ",
                        "selectable": True
                    },
                    {
                        "code": "ITEM_3",
                        "name_vi_vn": "Combo Bốc xếp và phí chờ",
                        "name_en_us": "Combo Bốc xếp và phí chờ",
                        "selectable": True
                    }
                ],
                "service_group_id": "TRUCK-1500",
                "group_id": "CHUYENNHA"
            },
            {
                "_id": "SGN-TRUCK-1500-INSURANCE",
                "name": "Khai giá hàng hoá",
                "name_vi_vn": "Khai giá hàng hoá",
                "name_en_us": "Value declaration",
                "enable": True,
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/Insurance/secure+24x24%402x.png",
                "order": 1,
                "price_blocks": [
                    {
                        "from": 0,
                        "to": 10000001,
                        "price": 2000,
                        "description_vi_vn": "Bồi thường mất mát hoặc hư hỏng theo giá trị hàng hoá của bạn",
                        "description_en_us": "Coverage for loss or damage according to the value of your items"
                    }
                ],
                "no_supplier_payout": True,
                "type": "COD_INSURANCE",
                "applied_stp_num": 10,
                "required_item_value": True,
                "service_id": "SGN-TRUCK-1500",
                "description_url": "https://ahamove.com/phi-khai-gia-cho-truck-ahmxsaladin/",
                "benefit_url": "https://ahamove.com/phi-khai-gia-cho-truck-ahmxsaladin/",
                "non_cod_description": "Bồi thường mất mát hoặc hư hỏng theo danh mục hàng hoá của bạn",
                "none_cod_price_blocks": {
                    "electronics": 2000,
                    "health & beauty": 2000,
                    "housing & lifestyle": 2000,
                    "food": 2000,
                    "mother & baby": 2000,
                    "fashion": 2000,
                    "grocery": 2000,
                    "restaurant": 2000,
                    "sport": 2000,
                    "drink": 2000,
                    "other": 2000,
                    "individual needs": 2000,
                    "transportation": 2000
                },
                "service_group_id": "TRUCK-1500"
            },
            {
                "_id": "SGN-TRUCK-1500-BOCXEP-KLLHC",
                "name": "Bốc xếp không lên lầu - 2 chiều",
                "name_vi_vn": "Bốc xếp không lên lầu - 2 chiều",
                "name_en_us": "2 Ways moving help (ground floor only)",
                "icon_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_loading_per_helper.png",
                "order": 2,
                "price": 185000,
                "description_vi_vn": "Tài xế hỗ trợ bốc xếp hàng hóa (đã được đóng thùng) xuống xe đến địa điểm chỉ định trong vòng 100m VÀ ngược lại (Áp dụng cho 2 lượt và không lên lầu). Các trường hợp phát sinh thêm, vui lòng thoả thuận với tài xế.",
                "description_en_us": "Driver provides moving help (already packaged) from vehicle to designated location within 100m AND vice versa (Apply for 2 turns and ground floor only). For additional cases, please negotiate with the driver.",
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-TRUCK-1500",
                "img_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_loading_per_helper.png",
                "enable": True,
                "service_group_id": "TRUCK-1500",
                "group_id": "BOCXEP"
            },
            {
                "_id": "SGN-TRUCK-1500-LOADERS",
                "name": "Thêm người bốc xếp",
                "enable": True,
                "name_vi_vn": "Thêm người bốc xếp",
                "name_en_us": "Thêm người bốc xếp",
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/more-pickers.png",
                "img_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/more-pickers.png",
                "order": 2,
                "price": 350000,
                "max_input": 3,
                "description_vi_vn": "Hàng hoá số lượng lớn hay có kích thước cồng kềnh, nặng và yêu cầu phải có 2 người bưng trở lên",
                "no_commission": False,
                "description_en_us": "Hàng hoá số lượng lớn hay có kích thước cồng kềnh, nặng và yêu cầu phải có 2 người bưng trở lên",
                "type": "PER_UNIT",
                "description": "Hàng hoá số lượng lớn hay có kích thước cồng kềnh, nặng và yêu cầu phải có 2 người bưng trở lên",
                "service_id": "SGN-TRUCK-1500",
                "service_group_id": "TRUCK-1500",
                "group_id": "LOADER"
            },
            {
                "_id": "SGN-TRUCK-1500-BOCXEP-LLMC",
                "name": "Bốc xếp tại nhà 1 tầng/lầu - 1 chiều",
                "name_vi_vn": "Bốc xếp tại nhà 1 tầng/lầu - 1 chiều",
                "name_en_us": "1 Way moving help (Maximum 1 Floor)",
                "icon_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_moving_help_upstair.png",
                "order": 3,
                "price": 185000,
                "description_vi_vn": "Tài xế hỗ trợ bốc xếp hàng hóa (đã được đóng thùng) xuống xe đến địa điểm chỉ định trong vòng 100m HOẶC ngược lại (Áp dụng cho 1 lượt, 1 lầu). Các trường hợp phát sinh thêm, vui lòng thoả thuận với tài xế.",
                "description_en_us": "Driver provides moving help (already packaged) from vehicle to designated location within 100m OR vice versa (Apply for 1 turn and maximum 1 floor). For additional cases, please negotiate with the driver.",
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-TRUCK-1500",
                "img_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_moving_help_upstair.png",
                "enable": True,
                "service_group_id": "TRUCK-1500",
                "group_id": "BOCXEP"
            },
            {
                "_id": "SGN-TRUCK-1500-BOCXEP-LLHC",
                "name": "Bốc xếp tại nhà 1 tầng/lầu - 2 chiều",
                "enable": True,
                "name_vi_vn": "Bốc xếp tại nhà 1 tầng/lầu - 2 chiều",
                "name_en_us": "2 Ways moving help (ground floor only)",
                "icon_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_loading_per_helper.png",
                "img_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_loading_per_helper.png",
                "order": 4,
                "price": 260000,
                "description_vi_vn": "Tài xế hỗ trợ bốc xếp hàng hóa (đã được đóng thùng) xuống xe đến địa điểm chỉ định trong vòng 100m VÀ ngược lại (Áp dụng cho 2 lượt và không lên lầu). Các trường hợp phát sinh thêm, vui lòng thoả thuận với tài xế.",
                "description_en_us": "Driver provides moving help (already packaged) from vehicle to designated location within 100m AND vice versa (Apply for 2 turns and ground floor only). For additional cases, please negotiate with the driver.",
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-TRUCK-1500",
                "service_group_id": "TRUCK-1500",
                "group_id": "BOCXEP"
            },
            {
                "_id": "SGN-TRUCK-1500-ROUND-TRIP",
                "name": "Quay lại điểm lấy hàng",
                "name_vi_vn": "Quay lại điểm lấy hàng",
                "name_en_us": "Return to pick up location",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_round_trip.png",
                "img_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_round_trip.png",
                "order": 5,
                "description_vi_vn": "Tài xế sẽ quay lại điểm lấy hàng với cước phí bằng 50% phí khoảng cách. Lưu ý: Phí khoảng cách là cước phí dựa theo số km vận chuyển, không bao gồm phí điểm dừng và các loại phí khác.",
                "description_en_us": "Driver will return to pick up location for 50% of distance fee. Note: Distance fee is calculated solely by the travel distance, it does not include stop fee and others fee",
                "type": "COMMISSION_DISTANCE_PERCENTAGE",
                "price": 0.5,
                "description": "",
                "enable": True,
                "service_id": "SGN-TRUCK-1500",
                "supplier_description_vi_vn": "Đối tác tiến hành quay trở lại điểm lấy hàng sau khi giao thành công ",
                "supplier_description": "Đối tác tiến hành quay trở lại điểm lấy hàng sau khi giao thành công ",
                "supplier_description_url": "https://ahamove.com/dichvukemtheo",
                "service_group_id": "TRUCK-1500",
                "group_id": "ROUND-TRIP"
            },
            {
                "_id": "SGN-TRUCK-1500-PHICHO",
                "name": "Phí chờ (60,000 VNĐ/giờ)",
                "name_vi_vn": "Phí chờ (60,000 VNĐ/giờ)",
                "enable": True,
                "name_en_us": "Waiting fee (60,000 VND/hour)",
                "icon_url": "https://ahamove.com/wp-content/uploads/2022/01/waiting.png",
                "img_url": "https://ahamove.com/wp-content/uploads/2022/01/waiting.png",
                "order": 6,
                "price": 60000,
                "no_commission": True,
                "description_vi_vn": "Vui lòng chọn phụ phí thời gian chờ tương ứng để khích lệ tài xế trong trường hợp khách hàng có mong muốn tài xế chờ lâu hơn 45 phút kể từ thời điểm tài xế đến nơi lấy hàng.",
                "description_en_us": "In case customers want the driver to wait longer than 45 minutes from the time driver arrived, please choose the corresponding waiting fee to encourage the driver.",
                "max_input": 5,
                "type": "PER_UNIT",
                "description": "",
                "service_id": "SGN-TRUCK-1500",
                "service_group_id": "TRUCK-1500",
                "group_id": "PHICHO"
            },
            {
                "_id": "SGN-TRUCK-1500-TIP",
                "name": "Hỗ trợ tài xế",
                "enable": True,
                "name_vi_vn": "Hỗ trợ tài xế",
                "name_en_us": "Tipping",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/sr_tipping.png",
                "img_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/sr_tipping.png",
                "order": 11,
                "price": 10000,
                "max_input": 10,
                "description_vi_vn": "Hãy chọn dịch vụ này nếu bạn muốn hỗ trợ tài xế trong giờ cao điểm, khi thời tiết khó khăn, hoặc đơn giản là muốn thưởng thêm cho tài xế. Ngoài ra, tính năng này sẽ giúp cho đơn hàng của bạn được ưu tiên hơn trong thời gian cao điểm.",
                "no_commission": True,
                "description_en_us": "This will show your support or compliment to the driver, especially in rush hours, bad weather. Also, this feature will prioritize your request in peak time.",
                "type": "PER_UNIT",
                "description": "",
                "service_id": "SGN-TRUCK-1500",
                "service_group_id": "TRUCK-1500",
                "group_id": "TIP"
            }
        ],
        "currency": "VND"
    },
    {
        "_id": "SGN-TRUCK-B2B-1500",
        "enable": True,
        "order": 11,
        "city_id": "SGN",
        "name": "Xe Tải 1500kg (Doanh nghiệp)",
        "name_vi_vn": "Xe Tải 1500kg (Doanh nghiệp)",
        "name_en_us": "Xe Tải 1500kg (Doanh nghiệp)",
        "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/aha-service/xe_ta%CC%89i_1500kg+(1).png",
        "map_icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/services/Truck_service_map_icon/Truck.png",
        "parent_id": "",
        "stop_fee": 33000,
        "commission_type": "PERCENTAGE",
        "commission_value": 0.16275,
        "distance_fee": "320000 if x <= 4 else 320000 + (x - 4) * 21000 if x <= 10 else 320000 + 6 * 21000 + (x - 10) * 18000 if x <= 15 else 320000 + 6 * 21000 + 5 * 18000  + (x - 15) * 11500",
        "broadcast_distance": 5500,
        "accept_interval": 1800,
        "require_to": True,
        "max_stop_points": 10,
        "notify_package_return": True,
        "description_en_us": "📦 (LxWxH) 3.2 x 1.6 x 1.7 meters",
        "description_vi_vn": "📦 (DxRxC) 3.2 x 1.6 x 1.7 mét",
        "fee_description_en_us": "\"Payload capacity: 1,500kg\nSuitable goods (LxWxH): 3.2 x 1.6 x 1.7 meters\n\nDistance fee:\n- From 00 - 04km: 320,000 VND\n- From 04 - 10km: 21,000 VND/km\n- From 10 - 15km: 18,000 VND/km\n- Over 15km: 11,500 VND/km\n\nStop-fee: 33,000 VND/stop\n\nTruck ban hours (Urban areas)\n- From 06:00 - 09:00 AM\n- From 16:00 - 19:00 PM (HN) / 20:00 PM (TP.HCM)\n*Tip: Use VAN during truck ban hours to optimize orders\n\nMaximum COD: 10,000,000 VND\nCOD fee:\n- COD <   2,000,000 VND: Free\n- COD >= 2,000,000 VND: 0.88% x Value of COD\"",
        "fee_description_vi_vn": "\"Khối lượng chuyên chở: 1,500kg\nHàng hoá phù hợp (DxRxC): 3.2 x 1.6 x 1.7 mét\n\nPhí quãng đường:\n- Từ 00 - 04km: 320,000đ\n- Từ 04 - 10km: 21,000đ/km\n- Từ 10 - 15km: 18,000đ/km\n- Trên 15km: 11,500đ/km\n\nPhí điểm dừng: 33,000đ/điểm dừng\n\nKhung giờ cấm tải (Nội thành)\n- Từ 06:00 - 09:00 AM\n- Từ 16:00 - 19:00 PM (HN) / 20:00 PM (TP.HCM)\n*Mách bạn: Hãy sử dụng xe tải VAN trong khung giờ cấm tải để tối ưu đơn hàng\n\nMức COD tối đa: 10,000,000đ\nPhí COD:\n- COD <   2,000,000đ: Miễn phí\n- COD >= 2,000,000đ: 0.88% x Giá trị COD\"",
        "vehicle_info": {
            "image": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/services/truck/Truck-1500.png",
            "length": 3.2,
            "width": 1.6,
            "height": 1.7,
            "weight": 100,
            "box_volume": 10,
            "short_intro_vi": "Thích hợp cho hàng hoá lớn và không hoạt động trong khung giờ cấm tải ",
            "short_intro_en": "This vehicle is suitable to carry big parcels and deactive in truck ban hours",
            "short_description_vi": "3.2 x 1.6 x 1.7 mét. Lên tới 1500kg",
            "short_description_en": "3.2 x 1.6 x 1.7 Meter. Up to 1500kgs",
            "description_vi_vn": "\"Khối lượng chuyên chở: 1,500kg\nHàng hoá phù hợp (DxRxC): 3.2 x 1.6 x 1.7 mét\n\nPhí quãng đường:\n- Từ 00 - 04km: 320,000đ\n- Từ 04 - 10km: 21,000đ/km\n- Từ 10 - 15km: 18,000đ/km\n- Trên 15km: 11,500đ/km\n\nPhí điểm dừng: 33,000đ/điểm dừng\n\nKhung giờ cấm tải (Nội thành)\n- Từ 06:00 - 09:00 AM\n- Từ 16:00 - 19:00 PM (HN) / 20:00 PM (TP.HCM)\n*Mách bạn: Hãy sử dụng xe tải VAN trong khung giờ cấm tải để tối ưu đơn hàng\n\nMức COD tối đa: 10,000,000đ\nPhí COD:\n- COD <   2,000,000đ: Miễn phí\n- COD >= 2,000,000đ: 0.88% x Giá trị COD\"",
            "description_en_us": "\"Payload capacity: 1,500kg\nSuitable goods (LxWxH): 3.2 x 1.6 x 1.7 meters\n\nDistance fee:\n- From 00 - 04km: 320,000 VND\n- From 04 - 10km: 21,000 VND/km\n- From 10 - 15km: 18,000 VND/km\n- Over 15km: 11,500 VND/km\n\nStop-fee: 33,000 VND/stop\n\nTruck ban hours (Urban areas)\n- From 06:00 - 09:00 AM\n- From 16:00 - 19:00 PM (HN) / 20:00 PM (TP.HCM)\n*Tip: Use VAN during truck ban hours to optimize orders\n\nMaximum COD: 10,000,000 VND\nCOD fee:\n- COD <   2,000,000 VND: Free\n- COD >= 2,000,000 VND: 0.88% x Value of COD\""
        },
        "cross_service": {
            "enable": False,
            "services": []
        },
        "cross_city": {
            "enable": True,
            "cities": [
                "SGN",
                "THD",
                "BHC"
            ]
        },
        "timeout": 1800,
        "cod": 10000000,
        "max_cod": 100000000,
        "delivery_type": "TRUCK",
        "available_districts": [
            "VN.HC.QE",
            "VN.HC.TD",
            "VN.HC.BT",
            "VN.HC.QK",
            "VN.HC.TD",
            "VN.HC.BH",
            "VN.HC.QG",
            "VN.HC.TD",
            "VN.HC.TP",
            "VN.HC.QA",
            "VN.HC.QJ",
            "VN.HC.HM",
            "VN.HC.NB",
            "VN.HC.QC",
            "VN.HC.QH",
            "VN.HC.CC",
            "VN.HC.BC",
            "VN.HC.GV",
            "VN.HC.QF",
            "VN.HC.PN",
            "VN.HC.QD",
            "VN.HC.TB",
            "VN.HC.QL",
            "VN.TB",
            "VN.BH",
            "VN.LT",
            "VN.NT"
        ],
        "cod_commission": {
            "value": 0.0088,
            "none_commission_limit": 2000000
        },
        "advance_broadcast_distance": 5500,
        "payment_method": [
            {
                "description": "Cash",
                "description_vi_vn": "Tiền mặt",
                "payment": "cash",
                "order": 1
            },
            {
                "description": "Balance",
                "description_vi_vn": "Ví AhaMove",
                "payment": "balance",
                "order": 2
            },
            {
                "description": "MoMo e-Wallet",
                "description_vi_vn": "Ví điện tử MoMo",
                "payment": "momo",
                "order": 3
            },
            {
                "description": "ZaloPay e-Wallet",
                "description_vi_vn": "Ví điện tử ZaloPay",
                "payment": "Zalopay",
                "order": 4
            }
        ],
        "recommendation_config": {
            "supplier_timeout": 30,
            "recommend_timeout": 90,
            "recommend_radius": 3500,
            "sleep_interval": 90,
            "dispatch_mode": "RECOMMEND",
            "pool_mode": "NO_POOL",
            "pool_saving_threshold": 0.2,
            "poolable": False
        },
        "enable_platform": [
            "momo_deeplink",
            "momo_permission",
            "zalo",
            "zalopay",
            "smartpay_deeplink",
            "viettel-pay_deeplink"
        ],
        "advance_max_concurrent_orders": 1,
        "max_concurrent_orders": 1,
        "same_district_delivery": False,
        "same_district_delivery_areas": "",
        "supplier_description": "Thực hiện trong 120 phút, nhận tối đa 1 đơn",
        "supplier_description_url": "https://ahamove.com/dich-vu-ba-gac-tai-tai-van/",
        "enable_cancellation_punishment": True,
        "vat_rate": 0.1,
        "tooltips": {
            "ASSIGNING": {
                "message": [
                    "Đơn hàng của bạn đã được AhaMove xác nhận.",
                    "Hệ thống đang tìm kiếm đối tác giao hàng.",
                    "Vui lòng chờ trong vòng 10 - 20 phút."
                ],
                "message_vi_vn": [
                    "Đơn hàng của bạn đã được AhaMove xác nhận.",
                    "Hệ thống đang tìm kiếm đối tác giao hàng.",
                    "Vui lòng chờ trong vòng 10 - 20 phút."
                ]
            },
            "ACCEPTED": {
                "message": [
                    "Xin chúc mừng! Đã có tài xế nhận đơn hàng của bạn.",
                    "Tài xế sẽ đến điểm lấy hàng trong vòng 15 - 60 phút.",
                    "Hãy liên hệ tài xế nếu bạn có bất kỳ thay đổi nào."
                ],
                "message_vi_vn": [
                    "Xin chúc mừng! Đã có tài xế nhận đơn hàng của bạn.",
                    "Tài xế sẽ đến điểm lấy hàng trong vòng 15 - 60 phút.",
                    "Hãy liên hệ tài xế nếu bạn có bất kỳ thay đổi nào."
                ]
            }
        },
        "rebroadcast_interval": 1200,
        "rebroadcast_limit": 3,
        "distance_fee_v3": {
            "blocks": [
                {
                    "from": 0,
                    "to": 4,
                    "base": 320000,
                    "price_multiplier": 0
                },
                {
                    "from": 4,
                    "to": 10,
                    "base": 320000,
                    "price_multiplier": 21000
                },
                {
                    "from": 10,
                    "to": 15,
                    "base": 446000,
                    "price_multiplier": 18000
                },
                {
                    "from": 15,
                    "to": 10000,
                    "base": 536000,
                    "price_multiplier": 11500
                }
            ],
            "hour_rates": []
        },
        "truck_ban": {
            "ban_districts": [
                {
                    "_id": 269,
                    "hasc_2": "VN.HC.QK",
                    "name_2": "Quận 11",
                    "city_id": "SGN",
                    "name": "QK",
                    "tick": True,
                    "spc_VvMpv": 0,
                    "idx_VvMpv": 2
                },
                {
                    "_id": 275,
                    "hasc_2": "VN.HC.QE",
                    "name_2": "Quận 5",
                    "city_id": "SGN",
                    "name": "QE",
                    "tick": True,
                    "spc_VvMpv": 0,
                    "idx_VvMpv": 3
                },
                {
                    "_id": 260,
                    "hasc_2": "VN.HC.BH",
                    "name_2": "Bình Thạnh",
                    "city_id": "SGN",
                    "name": "BH",
                    "tick": True,
                    "spc_VvMpv": 0,
                    "idx_VvMpv": 4
                },
                {
                    "_id": 282,
                    "hasc_2": "VN.HC.TD",
                    "name_2": "Thủ Đức",
                    "city_id": "SGN",
                    "name": "TD",
                    "tick": True,
                    "spc_VvMpv": 0,
                    "idx_VvMpv": 5
                },
                {
                    "_id": 264,
                    "hasc_2": "VN.HC.GV",
                    "name_2": "Gò Vấp",
                    "city_id": "SGN",
                    "name": "GV",
                    "tick": True,
                    "spc_VvMpv": 0,
                    "idx_VvMpv": 7
                },
                {
                    "_id": 273,
                    "hasc_2": "VN.HC.QC",
                    "name_2": "Quận 3",
                    "city_id": "SGN",
                    "name": "QC",
                    "tick": True,
                    "spc_VvMpv": 0,
                    "idx_VvMpv": 8
                },
                {
                    "_id": 271,
                    "hasc_2": "VN.HC.QA",
                    "name_2": "Quận 1",
                    "city_id": "SGN",
                    "name": "QA",
                    "tick": True,
                    "spc_VvMpv": 0,
                    "idx_VvMpv": 9
                },
                {
                    "_id": 272,
                    "hasc_2": "VN.HC.TD",
                    "name_2": "Quận 2",
                    "city_id": "SGN",
                    "name": "QB",
                    "tick": True,
                    "spc_VvMpv": 0,
                    "idx_VvMpv": 10
                },
                {
                    "_id": 281,
                    "hasc_2": "VN.HC.TP",
                    "name_2": "Tân Phú",
                    "city_id": "SGN",
                    "name": "TP",
                    "tick": True,
                    "spc_VvMpv": 0,
                    "idx_VvMpv": 11
                },
                {
                    "_id": 274,
                    "hasc_2": "VN.HC.QD",
                    "name_2": "Quận 4",
                    "city_id": "SGN",
                    "name": "QD",
                    "tick": True,
                    "spc_VvMpv": 0,
                    "idx_VvMpv": 12
                },
                {
                    "_id": 261,
                    "hasc_2": "VN.HC.BT",
                    "name_2": "Bình Tân",
                    "city_id": "SGN",
                    "name": "BT",
                    "tick": True,
                    "spc_VvMpv": 0,
                    "idx_VvMpv": 13
                },
                {
                    "_id": 277,
                    "hasc_2": "VN.HC.QG",
                    "name_2": "Quận 7",
                    "city_id": "SGN",
                    "name": "QG",
                    "tick": True,
                    "spc_VvMpv": 0,
                    "idx_VvMpv": 15
                },
                {
                    "_id": 279,
                    "hasc_2": "VN.HC.TD",
                    "name_2": "Quận 9",
                    "city_id": "SGN",
                    "name": "QI",
                    "tick": True,
                    "spc_VvMpv": 0,
                    "idx_VvMpv": 16
                },
                {
                    "_id": 280,
                    "hasc_2": "VN.HC.TB",
                    "name_2": "Tân Bình",
                    "city_id": "SGN",
                    "name": "TB",
                    "tick": True,
                    "spc_VvMpv": 0,
                    "idx_VvMpv": 17
                },
                {
                    "_id": 276,
                    "hasc_2": "VN.HC.QF",
                    "name_2": "Quận 6",
                    "city_id": "SGN",
                    "name": "QF",
                    "tick": True,
                    "spc_VvMpv": 0,
                    "idx_VvMpv": 18
                },
                {
                    "_id": 278,
                    "hasc_2": "VN.HC.QH",
                    "name_2": "Quận 8",
                    "city_id": "SGN",
                    "name": "QH",
                    "tick": True,
                    "spc_VvMpv": 0,
                    "idx_VvMpv": 19
                },
                {
                    "_id": 267,
                    "hasc_2": "VN.HC.PN",
                    "name_2": "Phú Nhuận",
                    "city_id": "SGN",
                    "name": "PN",
                    "tick": True,
                    "spc_VvMpv": 0,
                    "idx_VvMpv": 20
                },
                {
                    "_id": 268,
                    "hasc_2": "VN.HC.QJ",
                    "name_2": "Quận 10",
                    "city_id": "SGN",
                    "name": "QJ",
                    "tick": True,
                    "spc_VvMpv": 0,
                    "idx_VvMpv": 21
                },
                {
                    "_id": 259,
                    "hasc_2": "VN.HC.BC",
                    "name_2": "Bình Chánh",
                    "city_id": "SGN",
                    "name": "BC",
                    "tick": True,
                    "spc_VvMpv": 0,
                    "idx_VvMpv": 22
                },
                {
                    "_id": 270,
                    "hasc_2": "VN.HC.QL",
                    "name_2": "Quận 12",
                    "city_id": "SGN",
                    "name": "QL",
                    "tick": True,
                    "spc_VvMpv": 0,
                    "idx_VvMpv": 23
                }
            ],
            "ban_hours": [
                {
                    "from": 15,
                    "to": 20
                }
            ],
            "enable": True,
            "recommend_service": "SGN-VAN-B2B-1000"
        },
        "opening_hours": "8-15",
        "route_api_url": "http://ops-osrm-car.ops-tech:8080/route/v1/driving/",
        "pending_period": 86400,
        "is_tip_allowed": True,
        "assigning_before": [
            {
                "from": 0,
                "to": 13,
                "value": 3600
            },
            {
                "from": 13,
                "to": 15,
                "value": 1800
            },
            {
                "from": 15,
                "to": 24,
                "value": 3600
            }
        ],
        "partner": True,
        "group_id": "TRUCK-B2B-1500",
        "animated_url": "https://i.imgur.com/xiDxEYN.png",
        "requests": [
            {
                "_id": "SGN-TRUCK-B2B-1500-TRANSFER-COD",
                "name": "Thu hộ qua ví điện tử (new)",
                "enable": True,
                "transfer_cod": True,
                "support_remarks": True,
                "name_vi_vn": "Thu hộ qua ví điện tử (new)",
                "name_en_us": "Collect payment via e-wallet (new)",
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/icon-POD-extraservice.png",
                "order": 1,
                "price": 0,
                "no_commission": True,
                "type": "BOOLEAN",
                "service_id": "SGN-TRUCK-B2B-1500",
                "img_url": "http://file.hstatic.net/1000010797/file/hand-to-hand.png",
                "description_vi_vn": "Tài xế không cần ứng trước tiền thu hộ. Người nhận chỉ cần quét mã QR để thanh toán qua ví điện tử hoặc ứng dụng Mobile Banking khi tài xế đến giao hàng. Tiền thu hộ sẽ tự động chuyển vào tài khoản COD của bạn sau khi đơn hàng hoàn tất.",
                "description_en_us": "Your driver doesn't have to pay in advance. Upon delivery, the recipient scans a QR code to pay via an e-wallet or Mobile Banking app. Payment will be transferred to your COD account once the order is complete.",
                "subtype": "epayment_on_delivery"
            },
            {
                "_id": "SGN-TRUCK-B2B-1500-INSURANCE",
                "name": "Khai giá hàng hoá",
                "name_vi_vn": "Khai giá hàng hoá",
                "name_en_us": "Value declaration",
                "required_item_value": True,
                "enable": True,
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/Insurance/secure+24x24%402x.png",
                "order": 1,
                "price_blocks": [
                    {
                        "from": 0,
                        "to": 10000001,
                        "price": 2000,
                        "description_vi_vn": "Bồi thường mất mát hoặc hư hỏng theo giá trị hàng hoá của bạn",
                        "description_en_us": "Coverage for loss or damage according to the value of your items"
                    },
                    {
                        "from": 10000001,
                        "to": 30000001,
                        "price": 10000,
                        "description_vi_vn": "Bồi thường mất mát hoặc hư hỏng theo giá trị hàng hoá của bạn",
                        "description_en_us": "Coverage for loss or damage according to the value of your items"
                    },
                    {
                        "from": 30000001,
                        "to": 50000001,
                        "price": 20000,
                        "description_vi_vn": "Bồi thường mất mát hoặc hư hỏng theo giá trị hàng hoá của bạn",
                        "description_en_us": "Coverage for loss or damage according to the value of your items"
                    },
                    {
                        "from": 50000001,
                        "to": 100000001,
                        "price": 40000,
                        "description_vi_vn": "Bồi thường mất mát hoặc hư hỏng theo giá trị hàng hoá của bạn",
                        "description_en_us": "Coverage for loss or damage according to the value of your items"
                    }
                ],
                "no_supplier_payout": True,
                "type": "COD_INSURANCE",
                "applied_stp_num": 10,
                "service_id": "SGN-TRUCK-B2B-1500",
                "description_url": "https://www.ahamove.com/khai-gia-hang-hoa-dich-vu-xe-tai-doanh-nghiep/",
                "benefit_url": "https://www.ahamove.com/khai-gia-hang-hoa-dich-vu-xe-tai-doanh-nghiep/",
                "non_cod_description": "Bồi thường mất mát hoặc hư hỏng theo danh mục hàng hoá của bạn",
                "none_cod_price_blocks": {
                    "electronics": 2000,
                    "health & beauty": 2000,
                    "housing & lifestyle": 2000,
                    "food": 2000,
                    "mother & baby": 2000,
                    "fashion": 2000,
                    "grocery": 2000,
                    "restaurant": 2000,
                    "sport": 2000,
                    "drink": 2000,
                    "other": 2000,
                    "individual needs": 2000,
                    "transportation": 2000
                },
                "service_group_id": "TRUCK-B2B-1500"
            },
            {
                "_id": "SGN-TRUCK-B2B-1500-LOADERS",
                "name": "Thêm người bốc xếp",
                "enable": True,
                "name_vi_vn": "Thêm người bốc xếp",
                "name_en_us": "Thêm người bốc xếp",
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/more-pickers.png",
                "img_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/more-pickers.png",
                "order": 2,
                "price": 350000,
                "max_input": 2,
                "description_vi_vn": "Hàng hoá số lượng lớn hay có kích thước cồng kềnh, nặng và yêu cầu phải có 2 người bưng trở lên",
                "no_commission": False,
                "description_en_us": "Hàng hoá số lượng lớn hay có kích thước cồng kềnh, nặng và yêu cầu phải có 2 người bưng trở lên",
                "type": "PER_UNIT",
                "description": "Hàng hoá số lượng lớn hay có kích thước cồng kềnh, nặng và yêu cầu phải có 2 người bưng trở lên",
                "service_id": "SGN-TRUCK-B2B-1500"
            },
            {
                "_id": "SGN-TRUCK-B2B-1500-BOCXEP-KLLMC",
                "name": "Bốc xếp không lên lầu - 1 chiều",
                "name_en_us": "1 Way moving help (ground floor only)",
                "name_vi_vn": "Bốc xếp không lên lầu - 1 chiều",
                "icon_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_loading_per_helper.png",
                "order": 3,
                "price": 110000,
                "description_vi_vn": "Tài xế hỗ trợ bốc xếp hàng hóa (đã được đóng thùng) xuống xe đến địa điểm chỉ định trong vòng 100m HOẶC ngược lại (Áp dụng cho 1 lượt và không lên lầu). Các trường hợp phát sinh thêm, vui lòng thoả thuận với tài xế.",
                "description_en_us": "Driver provides moving help (already packaged) from vehicle to designated location within 100m OR vice versa (Apply for 1 turn and ground floor only). For additional cases, please negotiate with the driver.",
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-TRUCK-B2B-1500",
                "img_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_loading_per_helper.png",
                "enable": True,
                "category": "UNLOADING"
            },
            {
                "_id": "SGN-TRUCK-B2B-1500-BOCXEP-KLLHC",
                "name": "Bốc xếp không lên lầu - 2 chiều",
                "name_vi_vn": "Bốc xếp không lên lầu - 2 chiều",
                "name_en_us": "2 Ways moving help (ground floor only)",
                "icon_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_loading_per_helper.png",
                "order": 4,
                "price": 185000,
                "description_vi_vn": "Tài xế hỗ trợ bốc xếp hàng hóa (đã được đóng thùng) xuống xe đến địa điểm chỉ định trong vòng 100m VÀ ngược lại (Áp dụng cho 2 lượt và không lên lầu). Các trường hợp phát sinh thêm, vui lòng thoả thuận với tài xế.",
                "description_en_us": "Driver provides moving help (already packaged) from vehicle to designated location within 100m AND vice versa (Apply for 2 turns and ground floor only). For additional cases, please negotiate with the driver.",
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-TRUCK-B2B-1500",
                "img_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_loading_per_helper.png",
                "enable": True,
                "category": "UNLOADING"
            },
            {
                "_id": "SGN-TRUCK-B2B-1500-BOCXEP-LLMC",
                "name": "Bốc xếp tại nhà có lầu - 1 chiều",
                "name_vi_vn": "Bốc xếp tại nhà có lầu - 1 chiều",
                "name_en_us": "1 Way moving help (Maximum 1 Floor)",
                "icon_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_moving_help_upstair.png",
                "order": 5,
                "price": 185000,
                "description_vi_vn": "Tài xế hỗ trợ bốc xếp hàng hóa (đã được đóng thùng) xuống xe đến địa điểm chỉ định trong vòng 100m HOẶC ngược lại (Áp dụng cho 1 lượt, 1 lầu). Các trường hợp phát sinh thêm, vui lòng thoả thuận với tài xế.",
                "description_en_us": "Driver provides moving help (already packaged) from vehicle to designated location within 100m OR vice versa (Apply for 1 turn and maximum 1 floor). For additional cases, please negotiate with the driver.",
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-TRUCK-B2B-1500",
                "img_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_moving_help_upstair.png",
                "enable": True,
                "category": "UNLOADING"
            },
            {
                "_id": "SGN-TRUCK-B2B-1500-BOCXEP-LLHC",
                "name": "Bốc xếp tại nhà có lầu - 2 chiều",
                "enable": True,
                "name_vi_vn": "Bốc xếp tại nhà có lầu - 2 chiều",
                "name_en_us": "2 Ways moving help (Maximum 1 Floor)",
                "icon_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_moving_help_upstair.png",
                "img_url": "http://hstatic.net/797/1000010797/10/2015/10-9/sr_moving_help_upstair.png",
                "order": 6,
                "price": 260000,
                "description_vi_vn": "Tài xế hỗ trợ bốc xếp hàng hóa (đã được đóng thùng) xuống xe đến địa điểm chỉ định trong vòng 100m VÀ ngược lại (Áp dụng cho 2 lượt, 1 lầu). Các trường hợp phát sinh thêm, vui lòng thoả thuận với tài xế.",
                "description_en_us": "Driver provides moving help (already packaged) from vehicle to designated location within 100m AND vice versa (Apply for 1 turn and maximum 1 floor). For additional cases, please negotiate with the driver.",
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-TRUCK-B2B-1500",
                "category": "UNLOADING"
            },
            {
                "_id": "SGN-TRUCK-B2B-1500-PHICHO",
                "name": "Phí chờ (60,000 VNĐ/giờ)",
                "name_vi_vn": "Phí chờ (60,000 VNĐ/giờ)",
                "enable": True,
                "name_en_us": "Waiting fee (60,000 VND/hour)",
                "icon_url": "https://ahamove.com/wp-content/uploads/2022/01/waiting.png",
                "img_url": "https://ahamove.com/wp-content/uploads/2022/01/waiting.png",
                "order": 7,
                "price": 90000,
                "no_commission": True,
                "description_vi_vn": "Vui lòng chọn phụ phí thời gian chờ tương ứng để khích lệ tài xế trong trường hợp khách hàng có mong muốn tài xế chờ lâu hơn 45 phút kể từ thời điểm tài xế đến nơi lấy hàng.",
                "description_en_us": "In case customers want the driver to wait longer than 45 minutes from the time driver arrived, please choose the corresponding waiting fee to encourage the driver.",
                "max_input": 5,
                "type": "PER_UNIT",
                "description": "",
                "service_id": "SGN-TRUCK-B2B-1500"
            },
            {
                "_id": "SGN-TRUCK-B2B-1500-TIP",
                "name": "Hỗ trợ tài xế",
                "enable": True,
                "name_vi_vn": "Hỗ trợ tài xế",
                "name_en_us": "Tipping",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/sr_tipping.png",
                "img_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/sr_tipping.png",
                "order": 8,
                "price": 10000,
                "max_input": 10,
                "description_vi_vn": "Hãy chọn dịch vụ này nếu bạn muốn hỗ trợ tài xế trong giờ cao điểm, khi thời tiết khó khăn, hoặc đơn giản là muốn thưởng thêm cho tài xế. Ngoài ra, tính năng này sẽ giúp cho đơn hàng của bạn được ưu tiên hơn trong thời gian cao điểm.",
                "no_commission": True,
                "description_en_us": "This will show your support or compliment to the driver, especially in rush hours, bad weather. Also, this feature will prioritize your request in peak time.",
                "type": "PER_UNIT",
                "description": "",
                "service_id": "SGN-TRUCK-B2B-1500"
            },
            {
                "_id": "SGN-TRUCK-B2B-1500-ROUND-TRIP",
                "name": "Quay lại điểm lấy hàng",
                "name_vi_vn": "Quay lại điểm lấy hàng",
                "name_en_us": "Return to pick up location",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_round_trip.png",
                "img_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_round_trip.png",
                "order": 9,
                "description_vi_vn": "Tài xế sẽ quay lại điểm lấy hàng với cước phí bằng 50% phí khoảng cách. Lưu ý: Phí khoảng cách là cước phí dựa theo số km vận chuyển, không bao gồm phí điểm dừng và các loại phí khác.",
                "description_en_us": "Driver will return to pick up location for 50% of distance fee. Note: Distance fee is calculated solely by the travel distance, it does not include stop fee and others fee",
                "type": "COMMISSION_DISTANCE_PERCENTAGE",
                "price": 0.5,
                "description": "",
                "enable": True,
                "service_id": "SGN-TRUCK-B2B-1500",
                "supplier_description_vi_vn": "Đối tác tiến hành quay trở lại điểm lấy hàng sau khi giao thành công ",
                "supplier_description": "Đối tác tiến hành quay trở lại điểm lấy hàng sau khi giao thành công ",
                "supplier_description_url": "https://ahamove.com/dichvukemtheo",
                "price100": 50
            }
        ],
        "currency": "VND"
    },
    {
        "_id": "SGN-HUB-SP-14H",
        "commission_type": "PERCENTAGE",
        "require_to": True,
        "require_request": False,
        "partner": True,
        "parent_id": "",
        "city_id": "SGN",
        "name": "HUB theo điểm x1.3",
        "name_vi_vn": "HUB theo điểm x1.3",
        "name_en_us": "HUB SP x1.3",
        "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/sp_hub.png",
        "map_icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/tv_motorcycle.png",
        "order": 12,
        "broadcast_distance": 5000,
        "advance_broadcast_distance": 10000,
        "stop_fee": 17000,
        "stop_failed": 17000,
        "timeout": 10800,
        "cod": 50000000,
        "max_concurrent_orders": 2,
        "distance_fee": "0",
        "commission_value": 0.3105,
        "enable": True,
        "location": [
            {
                "lng": 106.71185519999995,
                "lat": 10.7443535
            },
            {
                "lng": 106.704609,
                "lat": 10.824076
            },
            {
                "lng": 106.7126683,
                "lat": 10.7443831
            },
            {
                "lng": 106.61837,
                "lat": 10.741394
            },
            {
                "lng": 106.645744,
                "lat": 10.777895
            },
            {
                "lng": 106.6428865,
                "lat": 10.7788695
            },
            {
                "lng": 106.64509079999993,
                "lat": 10.7788797
            },
            {
                "lng": 106.670807,
                "lat": 10.77499
            },
            {
                "lng": 106.715297,
                "lat": 10.738243
            },
            {
                "lng": 106.624703,
                "lat": 10.787934
            },
            {
                "lng": 106.70374,
                "lat": 10.756295
            },
            {
                "lng": 106.688508,
                "lat": 10.791544
            },
            {
                "lng": 106.644945,
                "lat": 10.755281
            },
            {
                "lng": 106.660735,
                "lat": 10.754732
            },
            {
                "lng": 106.739348,
                "lat": 10.860514
            },
            {
                "lng": 106.711245,
                "lat": 10.804908
            },
            {
                "lng": 106.643241,
                "lat": 10.781547
            },
            {
                "lng": 106.644795,
                "lat": 10.800572
            },
            {
                "lng": 106.612857,
                "lat": 10.758142
            },
            {
                "lng": 106.678136,
                "lat": 10.799385
            },
            {
                "lng": 106.630817,
                "lat": 10.758031
            },
            {
                "lng": 106.664376,
                "lat": 10.777264
            },
            {
                "lng": 106.615785,
                "lat": 10.866922
            },
            {
                "lng": 106.625486,
                "lat": 10.854663
            },
            {
                "lng": 106.704609,
                "lat": 10.824076
            },
            {
                "lng": 106.649221,
                "lat": 10.772798
            }
        ],
        "notify_package_return": True,
        "vat_rate": 0.1,
        "available_districts": [
            "VN.HC.NB",
            "VN.HC.CG",
            "VN.HC.CC",
            "VN.HC.BC",
            "VN.HC.HM",
            "VN.BH",
            "VN.CM",
            "VN.LT",
            "VN.TDM",
            "VN.PG",
            "VN.TA",
            "VN.BC",
            "VN.BB",
            "VN.LK",
            "VN.XL",
            "VN.TP",
            "VN.VC",
            "VN.VT.TT",
            "VN.VT.XM",
            "VN.VT.DD",
            "VN.VT.VT",
            "VN.VT.BR",
            "VN.VT.CD",
            "VN.VT.CD",
            "VN.VT.LD",
            "VN.DA",
            "VN.HC.QB",
            "VN.HC.QC",
            "VN.HC.QG",
            "VN.HC.BH",
            "VN.HC.GV",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.PN",
            "VN.HC.QJ",
            "VN.HC.QD",
            "VN.HC.BT",
            "VN.HC.QF",
            "VN.HC.QA",
            "VN.HC.QE",
            "VN.HC.TB",
            "VN.HC.TD",
            "VN.HC.QH",
            "VN.HC.QI",
            "VN.HC.TP"
        ],
        "drop_off_districts": [
            "VN.HC.NB",
            "VN.HC.CG",
            "VN.HC.CC",
            "VN.HC.BC",
            "VN.HC.HM",
            "VN.BH",
            "VN.CM",
            "VN.LT",
            "VN.TDM",
            "VN.PG",
            "VN.TA",
            "VN.BC",
            "VN.BB",
            "VN.LK",
            "VN.XL",
            "VN.TP",
            "VN.VC",
            "VN.VT.TT",
            "VN.VT.XM",
            "VN.VT.DD",
            "VN.VT.VT",
            "VN.VT.BR",
            "VN.VT.CD",
            "VN.VT.CD",
            "VN.VT.LD",
            "VN.DA",
            "VN.HC.QB",
            "VN.HC.QC",
            "VN.HC.QG",
            "VN.HC.BH",
            "VN.HC.GV",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.PN",
            "VN.HC.QJ",
            "VN.HC.QD",
            "VN.HC.BT",
            "VN.HC.QF",
            "VN.HC.QA",
            "VN.HC.QE",
            "VN.HC.TB",
            "VN.HC.TD",
            "VN.HC.QH",
            "VN.HC.QI",
            "VN.HC.TP"
        ],
        "max_cod": 20000000,
        "priority_score": 6,
        "truck_ban": {
            "ban_districts": [
                {
                    "_id": 259,
                    "hasc_2": "VN.HC.BC",
                    "name_2": "Bình Chánh",
                    "city_id": "SGN",
                    "name": "BC",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 0
                },
                {
                    "_id": 262,
                    "hasc_2": "VN.HC.CC",
                    "name_2": "Củ Chi",
                    "city_id": "SGN",
                    "name": "CC",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 1
                },
                {
                    "_id": 263,
                    "hasc_2": "VN.HC.CG",
                    "name_2": "Cần Giờ",
                    "city_id": "SGN",
                    "name": "SCG",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 2
                },
                {
                    "_id": 265,
                    "hasc_2": "VN.HC.HM",
                    "name_2": "Hóc Môn",
                    "city_id": "SGN",
                    "name": "HM",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 3
                },
                {
                    "_id": 266,
                    "hasc_2": "VN.HC.NB",
                    "name_2": "Nhà Bè",
                    "city_id": "SGN",
                    "name": "NB",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 4
                },
                {
                    "_id": 9718,
                    "hasc_2": "VN.TDM",
                    "name_2": "Thành phố Thủ Dầu Một",
                    "city_id": "SGN",
                    "name": "TDM",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 5
                },
                {
                    "_id": 9739,
                    "hasc_2": "VN.CM",
                    "name_2": "Huyện Cẩm Mỹ",
                    "city_id": "SGN",
                    "name": "CM",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 6
                },
                {
                    "_id": 9731,
                    "hasc_2": "VN.BH",
                    "name_2": "Thành phố Biên Hòa",
                    "city_id": "SGN",
                    "name": "DNBH",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 7
                },
                {
                    "_id": 9719,
                    "hasc_2": "VN.BB",
                    "name_2": "Huyện Bàu Bàng",
                    "city_id": "SGN",
                    "name": "BB",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 8
                },
                {
                    "_id": 9740,
                    "hasc_2": "VN.LT",
                    "name_2": "Huyện Long Thành",
                    "city_id": "SGN",
                    "name": "LT",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 9
                },
                {
                    "_id": 9725,
                    "hasc_2": "VN.TA",
                    "name_2": "Thị xã Thuận An",
                    "city_id": "SGN",
                    "name": "TA",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 10
                },
                {
                    "_id": 9741,
                    "hasc_2": "VN.XL",
                    "name_2": "Huyện Xuân Lộc",
                    "city_id": "SGN",
                    "name": "XL",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 11
                },
                {
                    "_id": 9735,
                    "hasc_2": "VN.VC",
                    "name_2": "Huyện Vĩnh Cửu",
                    "city_id": "SGN",
                    "name": "VC",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 12
                },
                {
                    "_id": 9721,
                    "hasc_2": "VN.BC",
                    "name_2": "Thị xã Bến Cát",
                    "city_id": "SGN",
                    "name": "BC",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 13
                },
                {
                    "_id": 9732,
                    "hasc_2": "VN.LK",
                    "name_2": "Thị xã Long Khánh",
                    "city_id": "SGN",
                    "name": "LK",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 14
                },
                {
                    "_id": 9734,
                    "hasc_2": "VN.TP",
                    "name_2": "Huyện Tân Phú",
                    "city_id": "SGN",
                    "name": "DNTP",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 15
                },
                {
                    "_id": 9722,
                    "hasc_2": "VN.PG",
                    "name_2": "Huyện Phú Giáo",
                    "city_id": "SGN",
                    "name": "PG",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 16
                },
                {
                    "_id": 8747,
                    "hasc_2": "VN.VT.VT",
                    "name_2": "Thành phố Vũng Tàu",
                    "city_id": "SGN",
                    "name": "VT",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 17
                },
                {
                    "_id": 8748,
                    "hasc_2": "VN.VT.BR",
                    "name_2": "Thành phố Bà Rịa",
                    "city_id": "SGN",
                    "name": "BR",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 18
                },
                {
                    "_id": 8750,
                    "hasc_2": "VN.VT.CD",
                    "name_2": "Huyện Châu Đức",
                    "city_id": "SGN",
                    "name": "CD",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 19
                },
                {
                    "_id": 8751,
                    "hasc_2": "VN.VT.XM",
                    "name_2": "Huyện Xuyên Mộc",
                    "city_id": "SGN",
                    "name": "XM",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 20
                },
                {
                    "_id": 8754,
                    "hasc_2": "VN.VT.TT",
                    "name_2": "Phú Mỹ",
                    "city_id": "SGN",
                    "name": "TT",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 21
                },
                {
                    "_id": 8752,
                    "hasc_2": "VN.VT.LD",
                    "name_2": "Huyện Long Điền",
                    "city_id": "SGN",
                    "name": "LD",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 22
                },
                {
                    "_id": 8753,
                    "hasc_2": "VN.VT.DD",
                    "name_2": "Huyện Đất Đỏ",
                    "city_id": "SGN",
                    "name": "DD",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 23
                },
                {
                    "_id": 8755,
                    "hasc_2": "VN.VT.CD",
                    "name_2": "Huyện Côn Đảo",
                    "city_id": "SGN",
                    "name": "CD",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 24
                },
                {
                    "_id": 9724,
                    "hasc_2": "VN.DA",
                    "name_2": "Thị xã Dĩ An",
                    "city_id": "SGN",
                    "name": "DA",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 25
                },
                {
                    "_id": 260,
                    "hasc_2": "VN.HC.BH",
                    "name_2": "Bình Thạnh",
                    "city_id": "SGN",
                    "name": "BH",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 43
                },
                {
                    "_id": 261,
                    "hasc_2": "VN.HC.BT",
                    "name_2": "Bình Tân",
                    "city_id": "SGN",
                    "name": "BT",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 44
                },
                {
                    "_id": 264,
                    "hasc_2": "VN.HC.GV",
                    "name_2": "Gò Vấp",
                    "city_id": "SGN",
                    "name": "GV",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 45
                },
                {
                    "_id": 267,
                    "hasc_2": "VN.HC.PN",
                    "name_2": "Phú Nhuận",
                    "city_id": "SGN",
                    "name": "PN",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 46
                },
                {
                    "_id": 268,
                    "hasc_2": "VN.HC.QJ",
                    "name_2": "Quận 10",
                    "city_id": "SGN",
                    "name": "QJ",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 47
                },
                {
                    "_id": 269,
                    "hasc_2": "VN.HC.QK",
                    "name_2": "Quận 11",
                    "city_id": "SGN",
                    "name": "QK",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 48
                },
                {
                    "_id": 270,
                    "hasc_2": "VN.HC.QL",
                    "name_2": "Quận 12",
                    "city_id": "SGN",
                    "name": "QL",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 49
                },
                {
                    "_id": 271,
                    "hasc_2": "VN.HC.QA",
                    "name_2": "Quận 1",
                    "city_id": "SGN",
                    "name": "QA",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 50
                },
                {
                    "_id": 272,
                    "hasc_2": "VN.HC.QB",
                    "name_2": "Quận 2",
                    "city_id": "SGN",
                    "name": "QB",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 51
                },
                {
                    "_id": 273,
                    "hasc_2": "VN.HC.QC",
                    "name_2": "Quận 3",
                    "city_id": "SGN",
                    "name": "QC",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 52
                },
                {
                    "_id": 274,
                    "hasc_2": "VN.HC.QD",
                    "name_2": "Quận 4",
                    "city_id": "SGN",
                    "name": "QD",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 53
                },
                {
                    "_id": 275,
                    "hasc_2": "VN.HC.QE",
                    "name_2": "Quận 5",
                    "city_id": "SGN",
                    "name": "QE",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 54
                },
                {
                    "_id": 276,
                    "hasc_2": "VN.HC.QF",
                    "name_2": "Quận 6",
                    "city_id": "SGN",
                    "name": "QF",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 55
                },
                {
                    "_id": 277,
                    "hasc_2": "VN.HC.QG",
                    "name_2": "Quận 7",
                    "city_id": "SGN",
                    "name": "QG",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 56
                },
                {
                    "_id": 278,
                    "hasc_2": "VN.HC.QH",
                    "name_2": "Quận 8",
                    "city_id": "SGN",
                    "name": "QH",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 57
                },
                {
                    "_id": 279,
                    "hasc_2": "VN.HC.QI",
                    "name_2": "Quận 9",
                    "city_id": "SGN",
                    "name": "QI",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 58
                },
                {
                    "_id": 280,
                    "hasc_2": "VN.HC.TB",
                    "name_2": "Tân Bình",
                    "city_id": "SGN",
                    "name": "TB",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 59
                },
                {
                    "_id": 281,
                    "hasc_2": "VN.HC.TP",
                    "name_2": "Tân Phú",
                    "city_id": "SGN",
                    "name": "TP",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 60
                },
                {
                    "_id": 282,
                    "hasc_2": "VN.HC.TD",
                    "name_2": "Thủ Đức",
                    "city_id": "SGN",
                    "name": "TD",
                    "tick": True,
                    "spc_LASrc": 0,
                    "idx_LASrc": 61
                }
            ],
            "ban_hours": []
        },
        "max_stop_points": 21,
        "distance_fee_v3": {
            "blocks": [
                {
                    "from": 0,
                    "to": 100000,
                    "base": 0,
                    "price_multiplier": 0
                }
            ],
            "hour_rates": []
        },
        "group_id": "HUB-SP",
        "animated_url": "https://i.imgur.com/xiDxEYN.png",
        "requests": [
            {
                "_id": "SGN-HUB-SP-14H-TRANSFER-COD",
                "name": "Thu hộ COD",
                "enable": True,
                "name_vi_vn": "Thu hộ COD",
                "name_en_us": "Collect COD",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_d2d.png",
                "order": 1,
                "no_commission": True,
                "price": 0,
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-HUB-SP-14H",
                "transfer_cod": True,
                "service_group_id": "HUB-SP",
                "group_id": "TRANSFER_COD"
            }
        ],
        "currency": "VND"
    },
    {
        "_id": "SGN-ECOM-AUTOTEST",
        "enable": True,
        "order": 99,
        "city_id": "SGN",
        "name": "Giao hàng eCommerce",
        "rebroadcast_interval": 1200,
        "broadcast_distance": 3000,
        "name_vi_vn": "Giao hàng eCommerce",
        "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/sp-bike.png",
        "map_icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/tv_bike_2.png",
        "distance_fee": "(18000 if x <= 4 else 18000 + (x - 4) * 4000)",
        "partner_distance_fee": "26000 if x <= 5 else 31000 if x <= 15 else 41000",
        "commission_type": "PERCENTAGE",
        "commission_value": 0.236,
        "max_distance": 100000,
        "stop_fee": 5000,
        "name_en_us": "Service eCommerce",
        "require_to": True,
        "name_vi_VN": "Giao hàng eCommerce",
        "auto_assign": False,
        "auto_assign_distance": 1000,
        "require_request": False,
        "advance_broadcast_distance": 3000,
        "timeout": 120,
        "cod": 10000000,
        "first_order_cod": 1,
        "partner": True,
        "max_stop_points": 10,
        "max_concurrent_orders": 3,
        "fee_description_en_us": "Minimum fee (within 6km): đ30.000\nPer km: đ5.000",
        "description_en_us": "Deliver within an hour",
        "description_vi_vn": "Giao hàng trong 1h",
        "fee_description_vi_vn": "Phí tối thiểu (dưới 6km): đ30.000\nCác km tiếp theo: đ5.000",
        "tooltips": {
            "ASSIGNING": {
                "message": [
                    "Đơn hàng của bạn đang được AhaMove xử lí. Sẽ có tài xế chấp nhận trong 5-10' tiếp theo!"
                ],
                "message_vi_vn": [
                    "Đơn hàng của bạn đang được AhaMove xử lí. Sẽ có tài xế chấp nhận trong 5-10' tiếp theo!"
                ]
            },
            "ACCEPTED": {
                "message": [
                    "Driver will arrive to your location within 15 minutes",
                    "Delivery time can take up to 2 hours"
                ],
                "message_vi_vn": [
                    "Tài xế sẽ đến chỗ bạn trong vòng 15 phút",
                    "Thời gian giao hàng có thể lên đến 2 tiếng"
                ]
            }
        },
        "supplier_description": "https://ahamove.com/quy-trinh-giao-don-hang-thuong-mai-dien-tu/",
        "rebroadcast_limit": 2,
        "idle_timeout": 180,
        "last_valid_rebroadcast_hour": 18,
        "next_valid_rebroadcast_hour": 18,
        "last_valid_rts_hour": 9,
        "note": "1. Vui lòng gọi điện cho người nhận trước khi đến lấy hàng.\n2. Đơn hàng không cần ứng tiền COD, vẫn thu tiền COD từ người nhận và nộp lại qua MoMo/Tk Ahamove.\n3. Tài xế huỷ đơn thì phải gọi lên tổng đài. Tuyệt đối không lấy hàng đi nếu chưa gọi được cho người nhận.\n4. Olala.\n5. Olele.",
        "sms_when_boarding": False,
        "last_valid_ro_hour": 19,
        "cross_service": {
            "enable": True,
            "non-category": [
                "Corporation - Cake",
                "Corporation - Dry food"
            ],
            "services": [
                "SGN-POOL",
                "SGN-SENDO-TMDT"
            ]
        },
        "valid_distance_to_perform_action": 5000000,
        "event_callback": True,
        "recommendation_config": {
            "supplier_timeout": 15,
            "recommend_timeout": 45,
            "poolable": True,
            "recommend_radius": 500
        },
        "set_idle_status_when_creating_order": False,
        "notify_package_return": True,
        "max_cod": 10000000.0,
        "priority_score": 6,
        "distance_fee_v3": {
            "blocks": [
                {
                    "from": 0,
                    "to": 4,
                    "base": 18000,
                    "price_multiplier": 0
                },
                {
                    "from": 4,
                    "to": 100000,
                    "base": 18000,
                    "price_multiplier": 4000
                }
            ],
            "hour_rates": []
        },
        "animated_url": "https://i.imgur.com/xiDxEYN.png",
        "requests": [],
        "currency": "VND"
    },
    {
        "_id": "SGN-HEINEKEN",
        "commission_type": "PERCENTAGE",
        "require_to": True,
        "require_request": False,
        "parent_id": "",
        "city_id": "SGN",
        "enable": True,
        "partner": True,
        "name": "Heineken",
        "name_vi_vn": "Heineken",
        "name_en_us": "Heineken",
        "icon_url": "https://www.heineken.com/us/~/resources/Heineken/USA/footer_images/heineken_tout_lager.jpg",
        "map_icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/tv_motorcycle.png",
        "order": 99,
        "pending_period": 200,
        "broadcast_distance": 5000,
        "advance_broadcast_distance": 5000,
        "supplier_description": "https://ahamove.com/quy-trinh-giao-don-heineken/",
        "stop_fee": 5000,
        "timeout": 1200,
        "distance_fee": "(23000 if x <= 5 else 23000 + (x - 5) * 5000)",
        "commission_value": 0.23600000000000002,
        "valid_distance_to_perform_action": 20000,
        "cross_service": {
            "enable": True,
            "services": [
                "SGN-BIKE"
            ]
        },
        "note": "1. Vui lòng gọi điện cho người nhận trước khi đến lấy hàng.\n2. Để người bàn giao hàng cập nhật trạng thái ĐÃ LẤY HÀNG.\n3. Giao “ĐÚNG NGƯỜI” và “ĐÚNG ĐỊA CHỈ” như trên đơn hàng. Trường hợp thay đổi thông tin giao nhận hàng hóa vui lòng liên hệ tổng đài. \n4. Chụp lại địa chỉ giao hàng thực tế cho Người Nhận khi hoàn thành đơn hàng.",
        "recommendation_config": {
            "supplier_timeout": 20,
            "recommend_timeout": 60,
            "poolable": True,
            "recommend_radius": 500,
            "sleep_interval": 300,
            "dispatch_mode": "RECOMMEND",
            "pool_mode": "NO_POOL",
            "pool_saving_threshold": 0.2
        },
        "max_concurrent_orders": 2,
        "priority_score": 6,
        "distance_fee_v3": {
            "blocks": [
                {
                    "from": 0,
                    "to": 5,
                    "base": 23000,
                    "price_multiplier": 0
                },
                {
                    "from": 5,
                    "to": 100000,
                    "base": 23000,
                    "price_multiplier": 5000
                }
            ],
            "hour_rates": []
        },
        "group_id": "OTHERS",
        "animated_url": "https://i.imgur.com/xiDxEYN.png",
        "requests": [],
        "currency": "VND"
    },
    {
        "_id": "SGN-SAMEDAY-INTERNAL",
        "enable": True,
        "order": 99,
        "city_id": "SGN",
        "name": "Same day - internal",
        "rebroadcast_interval": 12000,
        "rebroadcast_limit": 12,
        "broadcast_distance": 2000,
        "idle_timeout": 12000,
        "name_vi_vn": "4H",
        "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/sp-sameday.png",
        "map_icon_url": "https://ahamoveimg.s3-ap-southeast-1.amazonaws.com/services/icon+2.9.png",
        "distance_fee": "27500 if x <= 4 else 27500 + (x - 4) * 5500",
        "commission_type": "PERCENTAGE",
        "commission_value": 0.212,
        "max_distance": 100000,
        "stop_fee": 2750,
        "name_en_us": "4H",
        "require_to": True,
        "auto_assign": True,
        "auto_assign_distance": 5000,
        "require_request": False,
        "advance_broadcast_distance": 5000,
        "timeout": 120000,
        "cod": 5000000,
        "first_order_cod": 1,
        "partner": True,
        "max_stop_points": 20,
        "max_concurrent_orders": 2,
        "pending_period": 100,
        "notify_package_return": True,
        "cross_service": {
            "enable": True,
            "services": [
                "SGN-POOL",
                "SGN-LAZADA",
                "SGN-SENDO-TMDT"
            ],
            "non-category": [
                "Corporation - Cake",
                "Corporation - Dry food"
            ]
        },
        "recommend_order": False,
        "event_callback": True,
        "set_idle_status_when_creating_order": False,
        "parent_id": "",
        "delivery_type": "SAMEDAY",
        "delay_time": 20,
        "available_districts": [
            "VN.HC.BC",
            "VN.HC.CC",
            "VN.HC.CG",
            "VN.HC.HM",
            "VN.HC.NB",
            "VN.HC.QJ",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.QA",
            "VN.HC.QB",
            "VN.HC.QC",
            "VN.HC.QD",
            "VN.HC.QE",
            "VN.HC.QF",
            "VN.HC.QG"
        ],
        "assigning_list_order": 2,
        "recommendation_config": {
            "supplier_timeout": 20,
            "recommend_timeout": 100,
            "recommend_radius": 500,
            "sleep_interval": 300,
            "dispatch_mode": "RECOMMEND",
            "pool_mode": "NO_POOL",
            "pool_saving_threshold": 0.2,
            "poolable": False
        },
        "vat_rate": 0.1,
        "priority_score": 6,
        "distance_fee_v3": {
            "blocks": [
                {
                    "from": 0,
                    "to": 4,
                    "base": 27500,
                    "price_multiplier": 0
                },
                {
                    "from": 4,
                    "to": 100000,
                    "base": 27500,
                    "price_multiplier": 5500
                }
            ],
            "hour_rates": []
        },
        "group_id": "4H",
        "animated_url": "https://i.imgur.com/xiDxEYN.png",
        "requests": [
            {
                "_id": "SGN-SAMEDAY-INTERNAL-POD",
                "service_id": "SGN-SAMEDAY-INTERNAL",
                "enable": True,
                "name": "Thu hộ qua ví điện tử",
                "name_vi_vn": "Thu hộ qua ví điện tử",
                "name_en_us": "Collect payment via e-wallet",
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/icon-POD-extraservice.png",
                "img_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/IMG-POD-extraservice.png",
                "order": 0,
                "price": 0,
                "description_vi_vn": "Tài xế không cần ứng trước tiền thu hộ. Người nhận chỉ cần quét mã QR để thanh toán qua ví điện tử hoặc ứng dụng Mobile Banking khi tài xế đến giao hàng. Tiền thu hộ sẽ tự động chuyển vào tài khoản COD của bạn sau khi đơn hàng hoàn tất.",
                "description_en_us": "Your driver doesn't have to pay in advance. Upon delivery, the recipient scans a QR code to pay via an e-wallet or Mobile Banking app. Payment will be transferred to your COD account once the order is complete.",
                "type": "BOOLEAN",
                "description": "Người nhận thanh toán qua ví điện tử",
                "no_commission": True,
                "subtype": "epayment_on_delivery",
                "applied_stp_num": 1,
                "max_pod": 2000000
            },
            {
                "_id": "SGN-SD-POD-TRANSFER-COD",
                "name": "Payment on delivery",
                "enable": True,
                "support_remarks": True,
                "name_vi_vn": "Payment on delivery",
                "name_en_us": "Payment on delivery",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_d2d.png",
                "order": 1,
                "price": 0,
                "no_commission": True,
                "type": "BOOLEAN",
                "transfer_cod": True,
                "service_id": "SGN-SAMEDAY-INTERNAL",
                "img_url": "http://file.hstatic.net/1000010797/file/hand-to-hand.png"
            },
            {
                "_id": "SGN-SAMEDAY-INTERNAL-TRANSFER-COD",
                "name": "Nộp tiền thu hộ",
                "enable": True,
                "support_remarks": True,
                "name_vi_vn": "Nộp tiền thu hộ",
                "name_en_us": "Nộp tiền thu hộ",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_d2d.png",
                "order": 1,
                "price": 0,
                "no_commission": True,
                "type": "BOOLEAN",
                "service_id": "SGN-SAMEDAY-INTERNAL",
                "img_url": "http://file.hstatic.net/1000010797/file/hand-to-hand.png"
            }
        ],
        "currency": "VND"
    },
    {
        "_id": "SGN-TMDT",
        "commission_type": "PERCENTAGE",
        "require_to": True,
        "require_request": False,
        "notify_package_return": True,
        "cross_service": {
            "enable": True,
            "services": [
                "SGN-POOL",
                "SGN-LAZADA"
            ]
        },
        "parent_id": "",
        "city_id": "SGN",
        "enable": True,
        "name": "Thương Mại Điện Tử",
        "name_vi_vn": "Thương Mại Điện Tử",
        "name_en_us": "E-Commerce",
        "icon_url": "https://trello-attachments.s3.amazonaws.com/5959c169ff857d53dd292999/5b73e5c38f17db297fb28c52/7db086ccc5a30461d075e8696b38bd2b/Untitled-1-01.png",
        "map_icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/tv_bike_2.png",
        "order": 99,
        "broadcast_distance": 2000,
        "advance_broadcast_distance": 4000,
        "stop_fee": 5500,
        "pending_period": 0,
        "timeout": 28800,
        "rebroadcast_interval": 21600,
        "max_concurrent_orders": 3,
        "advance_max_concurrent_orders": 3,
        "max_stop_points": 20,
        "cod": 50000000,
        "max_cod": 250000000,
        "first_order_cod": 1,
        "distance_fee": "(20000 if x <= 4 else 20000 + (x - 4) * 4400)",
        "commission_value": 0.212,
        "recommendation_config": {
            "supplier_timeout": 20,
            "recommend_timeout": 100,
            "recommend_radius": 1000,
            "sleep_interval": 300,
            "dispatch_mode": "RECOMMEND",
            "pool_mode": "NO_POOL",
            "pool_saving_threshold": 0.2,
            "poolable": False
        },
        "delay_time": 3,
        "location": [
            {
                "lng": 106.664025,
                "lat": 10.769967
            },
            {
                "lng": 106.657038,
                "lat": 10.7726336
            },
            {
                "lng": 106.7001281,
                "lat": 10.7571664
            },
            {
                "lng": 106.6612372,
                "lat": 10.8009098
            },
            {
                "lng": 106.694785,
                "lat": 10.7690426
            },
            {
                "lng": 106.7120955,
                "lat": 10.8098009
            },
            {
                "lng": 106.6867061,
                "lat": 10.7706871
            },
            {
                "lng": 106.693248,
                "lat": 10.760305
            },
            {
                "lng": 106.7135168,
                "lat": 10.7986618
            },
            {
                "lng": 106.7135889,
                "lat": 10.798822
            },
            {
                "lng": 106.71303,
                "lat": 10.7986485
            },
            {
                "lng": 106.701583,
                "lat": 10.745586
            },
            {
                "lng": 106.6111886,
                "lat": 10.8176126
            },
            {
                "lng": 106.6107746,
                "lat": 10.8198324
            },
            {
                "lng": 106.6127303,
                "lat": 10.8198501
            },
            {
                "lng": 106.6202069,
                "lat": 10.8040739
            },
            {
                "lng": 106.6649492,
                "lat": 10.8485407
            },
            {
                "lng": 106.6164587,
                "lat": 10.8069437
            },
            {
                "lng": 106.6663901,
                "lat": 10.8488272
            },
            {
                "lng": 106.6211575,
                "lat": 10.8066531
            },
            {
                "lng": 106.6666894,
                "lat": 10.84881
            },
            {
                "lng": 106.6171609,
                "lat": 10.807021
            },
            {
                "lng": 106.6159155,
                "lat": 10.8087893
            },
            {
                "lng": 106.616526,
                "lat": 10.808233
            },
            {
                "lng": 106.649221,
                "lat": 10.772798
            },
            {
                "lng": 106.66392,
                "lat": 10.76962
            }
        ],
        "max_per_stop_point": 30000000,
        "opening_hours": "0-23",
        "payment_method": [
            {
                "description": "Cash",
                "description_vi_vn": "Tiền mặt",
                "payment": "cash",
                "order": 1
            },
            {
                "description": "Balance",
                "description_vi_vn": "Ví AhaMove",
                "payment": "balance",
                "order": 2
            },
            {
                "description": "MoMo e-Wallet",
                "description_vi_vn": "Ví điện tử MoMo",
                "payment": "momo",
                "order": 3
            },
            {
                "description": "ZaloPay e-Wallet",
                "description_vi_vn": "Ví điện tử ZaloPay",
                "payment": "Zalopay",
                "order": 4
            }
        ],
        "assigning_list_order": 1,
        "vat_rate": 0.1,
        "available_districts": [
            "VN.HC.NB",
            "VN.HC.CG",
            "VN.HC.CC",
            "VN.HC.BC",
            "VN.HC.HM",
            "VN.BH",
            "VN.CM",
            "VN.LT",
            "VN.TDM",
            "VN.PG",
            "VN.TA",
            "VN.BC",
            "VN.BB",
            "VN.LK",
            "VN.XL",
            "VN.TP",
            "VN.VC",
            "VN.VT.TT",
            "VN.VT.XM",
            "VN.VT.DD",
            "VN.VT.VT",
            "VN.VT.BR",
            "VN.VT.CD",
            "VN.VT.CD",
            "VN.VT.LD",
            "VN.DA",
            "VN.HC.QB",
            "VN.HC.QC",
            "VN.HC.QG",
            "VN.HC.BH",
            "VN.HC.GV",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.PN",
            "VN.HC.QJ",
            "VN.HC.QD",
            "VN.HC.BT",
            "VN.HC.QF",
            "VN.HC.QA",
            "VN.HC.QE",
            "VN.HC.TB",
            "VN.HC.TD",
            "VN.HC.QH",
            "VN.HC.QI",
            "VN.HC.TP"
        ],
        "drop_off_districts": [
            "VN.HC.NB",
            "VN.HC.CG",
            "VN.HC.CC",
            "VN.HC.BC",
            "VN.HC.HM",
            "VN.BH",
            "VN.CM",
            "VN.LT",
            "VN.TDM",
            "VN.PG",
            "VN.TA",
            "VN.BC",
            "VN.BB",
            "VN.LK",
            "VN.XL",
            "VN.TP",
            "VN.VC",
            "VN.VT.TT",
            "VN.VT.XM",
            "VN.VT.DD",
            "VN.VT.VT",
            "VN.VT.BR",
            "VN.VT.CD",
            "VN.VT.CD",
            "VN.VT.LD",
            "VN.DA",
            "VN.HC.QB",
            "VN.HC.QC",
            "VN.HC.QG",
            "VN.HC.BH",
            "VN.HC.GV",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.PN",
            "VN.HC.QJ",
            "VN.HC.QD",
            "VN.HC.BT",
            "VN.HC.QF",
            "VN.HC.QA",
            "VN.HC.QE",
            "VN.HC.TB",
            "VN.HC.TD",
            "VN.HC.QH",
            "VN.HC.QI",
            "VN.HC.TP"
        ],
        "priority_score": 6,
        "distance_fee_v3": {
            "blocks": [
                {
                    "from": 0,
                    "to": 4,
                    "base": 20000,
                    "price_multiplier": 0
                },
                {
                    "from": 4,
                    "to": 100000,
                    "base": 20000,
                    "price_multiplier": 4400
                }
            ],
            "hour_rates": []
        },
        "weight_fee": [
            {
                "from": 0.0,
                "to": 7.0,
                "base": 5000.0,
                "price_multiplier": 0.0
            },
            {
                "from": 7.0,
                "to": 100.0,
                "price_multiplier": 0.0,
                "base": 15000.0
            },
            {
                "from": 100.0,
                "to": 100000.0,
                "base": 30000.0,
                "price_multiplier": 5000.0
            }
        ],
        "dim_factor": 5000.0,
        "route_api_url": "https://apistg.ahamove.com/api/v3/internal/osrm/bike/route/v1/driving/",
        "group_id": "TMDT",
        "animated_url": "https://i.imgur.com/xiDxEYN.png",
        "requests": [
            {
                "_id": "SGN-TMDT-POD",
                "name": "Thu hộ qua ví điện tử",
                "name_vi_vn": "Thu hộ qua ví điện tử",
                "name_en_us": "Collect payment via e-wallet",
                "icon_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/icon-POD-extraservice.png",
                "img_url": "https://ahamoveimg.s3.ap-southeast-1.amazonaws.com/Special+Request/IMG-POD-extraservice.png",
                "order": 0,
                "price": 0,
                "description_vi_vn": "Tài xế không cần ứng trước tiền thu hộ. Người nhận chỉ cần quét mã QR để thanh toán qua ví điện tử hoặc ứng dụng Mobile Banking khi tài xế đến giao hàng. Tiền thu hộ sẽ tự động chuyển vào tài khoản COD của bạn sau khi đơn hàng hoàn tất.",
                "description_en_us": "Your driver doesn't have to pay in advance. Upon delivery, the recipient scans a QR code to pay via an e-wallet or Mobile Banking app. Payment will be transferred to your COD account once the order is complete.",
                "type": "BOOLEAN",
                "description": "Người nhận thanh toán qua ví điện tử",
                "service_id": "SGN-TMDT",
                "enable": True,
                "no_commission": True,
                "subtype": "POD",
                "applied_stp_num": 1,
                "service_group_id": "TMDT"
            },
            {
                "_id": "SGN-TMDT-TRANSFER-COD",
                "name": "Nộp tiền thu hộ",
                "enable": True,
                "name_vi_vn": "Nộp tiền thu hộ",
                "name_en_us": "Collect COD",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_d2d.png",
                "img_url": "http://file.hstatic.net/1000010797/file/hand-to-hand.png",
                "order": 1,
                "price": 0,
                "no_commission": True,
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-TMDT",
                "transfer_cod": True,
                "capital_coefficient": 1,
                "subtype": "epayment_on_delivery",
                "service_group_id": "TMDT",
                "group_id": "TRANSFER_COD"
            },
            {
                "_id": "SGN-TMDT-THERMALBAG",
                "name": "Túi giữ nhiệt",
                "name_vi_vn": "Túi giữ nhiệt",
                "description_vi_vn": "Túi giữ nhiệt",
                "name_en_us": "Thermal Bag",
                "icon_url": "https://trello-attachments.s3.amazonaws.com/5eabe9291dc6933e9e74eb2f/5f8531508904fa20c3cc89ad/1545287f04ffcc958416ab13b8bc3de5/2710.png",
                "order": 1,
                "price": 0,
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-TMDT",
                "enable": True,
                "no_commission": True,
                "service_group_id": "TMDT",
                "group_id": "THERMAL_BAG"
            },
            {
                "_id": "SGN-TMDT-TIP",
                "name": "Hỗ trợ tài xế (TMDT)",
                "enable": True,
                "name_vi_vn": "Hỗ trợ tài xế (PER_UNIT)",
                "name_en_us": "Hỗ trợ tài xế (PER_UNIT)",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/sr_tipping.png",
                "order": 4,
                "no_commission": True,
                "type": "PER_UNIT",
                "price": 5000,
                "description": "",
                "service_id": "SGN-TMDT",
                "description_vi_vn": "Hãy chọn dịch vụ này nếu bạn muốn hỗ trợ tài xế trong giờ cao điểm, khi cần giao hàng lên lầu, nơi phải tốn phí giữ xe, khi thời tiết khó khăn, hoặc đơn giản là muốn thưởng thêm cho tài xế. Ngoài ra, tính năng này sẽ giúp cho đơn hàng của bạn được ưu tiên hơn trong thời gian cao điểm.",
                "description_en_us": "This will show your support or compliment to the driver, especially in rush hours, hand to hand delivery, bad weather. Also, this feature will prioritize your request in peak time.",
                "img_url": "http://file.hstatic.net/1000010797/file/tipping_final.jpg",
                "max_input": 5,
                "no_promotion": True,
                "path_index": 0,
                "service_group_id": "TMDT"
            }
        ],
        "currency": "VND"
    },
    {
        "_id": "SGN-TRUCK",
        "commission_type": "PERCENTAGE",
        "name": "Xe tải",
        "name_vi_vn": "Xe tải",
        "name_en_us": "Truck",
        "stop_fee": 10000,
        "distance_fee": "135000 if x <= 4 else 135000 + (x - 4) * 16000 if x <= 10 else 135000 + 6 * 16000 + (x - 10) * 11500 if x <= 15 else 135000 + 6 * 16000 + 5 * 11500  + (x - 15) * 11000",
        "commission_value": 0.2,
        "order": 99,
        "enable": True,
        "parent_id": "",
        "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/sp-truck-500.png",
        "map_icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/tv-truck-500.png",
        "city_id": "SGN",
        "require_to": True,
        "broadcast_distance": 5000,
        "enable_platform": [
            "momo_deeplink",
            "momo_permission",
            "zalo",
            "zalopay",
            "smartpay_deeplink"
        ],
        "cross_service": {
            "enable": True,
            "services": []
        },
        "cross_city": {
            "enable": True,
            "cities": [
                "SGN",
                "THD",
                "BHC",
                "VTG"
            ]
        },
        "opening_hours": "0-23",
        "enable_cancellation_punishment": False,
        "truck_ban": {
            "ban_hours": [
                {
                    "from": 6,
                    "to": 9
                },
                {
                    "from": 15,
                    "to": 20
                }
            ],
            "recommend_service": "SGN-TRICYCLE",
            "ban_districts": [
                {
                    "_id": 260,
                    "hasc_2": "VN.HC.BH",
                    "name_2": "Bình Thạnh",
                    "city_id": "SGN",
                    "name": "BH",
                    "tick": True,
                    "spc_TzKZn": 0,
                    "idx_TzKZn": 26
                },
                {
                    "_id": 264,
                    "hasc_2": "VN.HC.GV",
                    "name_2": "Gò Vấp",
                    "city_id": "SGN",
                    "name": "GV",
                    "tick": True,
                    "spc_TzKZn": 0,
                    "idx_TzKZn": 28
                },
                {
                    "_id": 267,
                    "hasc_2": "VN.HC.PN",
                    "name_2": "Phú Nhuận",
                    "city_id": "SGN",
                    "name": "PN",
                    "tick": True,
                    "spc_TzKZn": 0,
                    "idx_TzKZn": 29
                },
                {
                    "_id": 268,
                    "hasc_2": "VN.HC.QJ",
                    "name_2": "Quận 10",
                    "city_id": "SGN",
                    "name": "QJ",
                    "tick": True,
                    "spc_TzKZn": 0,
                    "idx_TzKZn": 30
                },
                {
                    "_id": 269,
                    "hasc_2": "VN.HC.QK",
                    "name_2": "Quận 11",
                    "city_id": "SGN",
                    "name": "QK",
                    "tick": True,
                    "spc_TzKZn": 0,
                    "idx_TzKZn": 31
                },
                {
                    "_id": 270,
                    "hasc_2": "VN.HC.QL",
                    "name_2": "Quận 12",
                    "city_id": "SGN",
                    "name": "QL",
                    "tick": True,
                    "spc_TzKZn": 0,
                    "idx_TzKZn": 32
                },
                {
                    "_id": 271,
                    "hasc_2": "VN.HC.QA",
                    "name_2": "Quận 1",
                    "city_id": "SGN",
                    "name": "QA",
                    "tick": True,
                    "spc_TzKZn": 0,
                    "idx_TzKZn": 33
                },
                {
                    "_id": 272,
                    "hasc_2": "VN.HC.QB",
                    "name_2": "Quận 2",
                    "city_id": "SGN",
                    "name": "QB",
                    "tick": True,
                    "spc_TzKZn": 0,
                    "idx_TzKZn": 34
                },
                {
                    "_id": 273,
                    "hasc_2": "VN.HC.QC",
                    "name_2": "Quận 3",
                    "city_id": "SGN",
                    "name": "QC",
                    "tick": True,
                    "spc_TzKZn": 0,
                    "idx_TzKZn": 35
                },
                {
                    "_id": 274,
                    "hasc_2": "VN.HC.QD",
                    "name_2": "Quận 4",
                    "city_id": "SGN",
                    "name": "QD",
                    "tick": True,
                    "spc_TzKZn": 0,
                    "idx_TzKZn": 36
                },
                {
                    "_id": 275,
                    "hasc_2": "VN.HC.QE",
                    "name_2": "Quận 5",
                    "city_id": "SGN",
                    "name": "QE",
                    "tick": True,
                    "spc_TzKZn": 0,
                    "idx_TzKZn": 37
                },
                {
                    "_id": 276,
                    "hasc_2": "VN.HC.QF",
                    "name_2": "Quận 6",
                    "city_id": "SGN",
                    "name": "QF",
                    "tick": True,
                    "spc_TzKZn": 0,
                    "idx_TzKZn": 38
                },
                {
                    "_id": 277,
                    "hasc_2": "VN.HC.QG",
                    "name_2": "Quận 7",
                    "city_id": "SGN",
                    "name": "QG",
                    "tick": True,
                    "spc_TzKZn": 0,
                    "idx_TzKZn": 39
                },
                {
                    "_id": 278,
                    "hasc_2": "VN.HC.QH",
                    "name_2": "Quận 8",
                    "city_id": "SGN",
                    "name": "QH",
                    "tick": True,
                    "spc_TzKZn": 0,
                    "idx_TzKZn": 40
                },
                {
                    "_id": 280,
                    "hasc_2": "VN.HC.TB",
                    "name_2": "Tân Bình",
                    "city_id": "SGN",
                    "name": "TB",
                    "tick": True,
                    "spc_TzKZn": 0,
                    "idx_TzKZn": 42
                },
                {
                    "_id": 281,
                    "hasc_2": "VN.HC.TP",
                    "name_2": "Tân Phú",
                    "city_id": "SGN",
                    "name": "TP",
                    "tick": True,
                    "spc_TzKZn": 0,
                    "idx_TzKZn": 43
                },
                {
                    "_id": 282,
                    "hasc_2": "VN.HC.TD",
                    "name_2": "Thủ Đức",
                    "city_id": "SGN",
                    "name": "TD",
                    "tick": True,
                    "spc_TzKZn": 0,
                    "idx_TzKZn": 44
                }
            ],
            "enable": True
        },
        "available_districts": [
            "VN.HC.BH",
            "VN.HC.GV",
            "VN.HC.PN",
            "VN.HC.QJ",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.QA",
            "VN.HC.QB",
            "VN.HC.QC",
            "VN.HC.QD",
            "VN.HC.QE",
            "VN.HC.QF",
            "VN.HC.QG",
            "VN.HC.QH",
            "VN.HC.TB",
            "VN.HC.TP",
            "VN.HC.TD"
        ],
        "require_pod": True,
        "map_icon_3d": {
            "url": "https://firebasestorage.googleapis.com/v0/b/aha-chat-292008.appspot.com/o/3dicon%2Fvan-500.png?alt=media&token=ccf93bbc-5363-4ae7-b59d-746da3f32d28",
            "sprite_size": 64,
            "sprite_count": 64
        },
        "priority_score": 6,
        "distance_fee_v3": {
            "blocks": [
                {
                    "from": 0,
                    "to": 4,
                    "base": 135000,
                    "price_multiplier": 0
                },
                {
                    "from": 4,
                    "to": 10,
                    "base": 135000,
                    "price_multiplier": 16000
                },
                {
                    "from": 10,
                    "to": 15,
                    "base": 231000,
                    "price_multiplier": 11500
                },
                {
                    "from": 15,
                    "to": 100000,
                    "base": 288500,
                    "price_multiplier": 11000
                }
            ],
            "hour_rates": []
        },
        "group_id": "OTHERS",
        "animated_url": "https://i.imgur.com/xiDxEYN.png",
        "requests": [],
        "currency": "VND"
    },
    {
        "_id": "SGN-HUB-SP",
        "commission_type": "PERCENTAGE",
        "require_to": True,
        "require_request": False,
        "parent_id": "",
        "city_id": "SGN",
        "enable": True,
        "name": "HUB theo điểm",
        "name_vi_vn": "HUB theo điểm",
        "name_en_us": "HUB theo điểm",
        "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/sp_hub.png",
        "map_icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/tv_motorcycle.png",
        "order": 99,
        "broadcast_distance": 7000,
        "stop_fee": 13200,
        "distance_fee": "0",
        "commission_value": 0.3105,
        "accept_interval": 1800,
        "timeout": 36000,
        "cod": 50000000,
        "stop_failed": 13200,
        "advance_broadcast_distance": 10000,
        "max_concurrent_orders": 5,
        "partner": True,
        "max_stop_points": 21,
        "supplier_description": "Đối tác nhận nhiều kiện hàng từ kho GHN và giao trong vòng 8 tiếng",
        "location": [
            {
                "lng": 106.6490111,
                "lat": 10.7729088
            },
            {
                "lng": 106.6602513,
                "lat": 10.7470446
            },
            {
                "lng": 106.6858985,
                "lat": 10.8245594
            },
            {
                "lng": 106.6622575,
                "lat": 10.7694943
            },
            {
                "lng": 106.6577308,
                "lat": 10.7794055
            },
            {
                "lng": 106.6363522,
                "lat": 10.8380384
            },
            {
                "lng": 106.608941,
                "lat": 10.806044
            },
            {
                "lng": 106.6127303,
                "lat": 10.8198501
            },
            {
                "lng": 106.657038,
                "lat": 10.7726336
            },
            {
                "lng": 106.71185519999995,
                "lat": 10.7443535
            },
            {
                "lng": 106.704609,
                "lat": 10.824076
            },
            {
                "lng": 106.617809,
                "lat": 10.740059
            },
            {
                "lng": 106.6161817,
                "lat": 10.7413936
            },
            {
                "lng": 10.741394,
                "lat": 106.61837
            },
            {
                "lng": 106.7126683,
                "lat": 10.7443831
            },
            {
                "lng": 106.670807,
                "lat": 10.77499
            },
            {
                "lng": 106.70374,
                "lat": 10.756295
            },
            {
                "lng": 106.64509079999993,
                "lat": 10.7788797
            },
            {
                "lng": 106.660735,
                "lat": 10.754732
            },
            {
                "lng": 106.617809,
                "lat": 10.740059
            },
            {
                "lng": 106.6161817,
                "lat": 10.7413936
            },
            {
                "lng": 10.741394,
                "lat": 106.61837
            },
            {
                "lng": 106.7126683,
                "lat": 10.7443831
            },
            {
                "lng": 106.670807,
                "lat": 10.77499
            },
            {
                "lng": 106.70374,
                "lat": 10.756295
            },
            {
                "lng": 106.64509079999993,
                "lat": 10.7788797
            },
            {
                "lng": 106.660735,
                "lat": 10.754732
            },
            {
                "lng": 106.73951,
                "lat": 10.860823
            },
            {
                "lng": 106.607769,
                "lat": 10.7762149
            },
            {
                "lng": 106.66387170000007,
                "lat": 10.769508199999999
            },
            {
                "lng": 106.616518,
                "lat": 10.81664
            },
            {
                "lng": 106.7098572,
                "lat": 10.7499515
            },
            {
                "lng": 106.6024788,
                "lat": 10.7878561
            },
            {
                "lng": 106.708932,
                "lat": 10.749496
            },
            {
                "lng": 106.6148377,
                "lat": 10.7498843
            },
            {
                "lng": 106.6086784,
                "lat": 10.8197539
            }
        ],
        "notify_package_return": True,
        "cross_service": {
            "enable": True,
            "services": [
                "SGN-HUB-SP"
            ]
        },
        "advance_max_concurrent_orders": 5,
        "delivery_type": "HUB",
        "max_distance": 150000,
        "need_confirm_before_pickup": True,
        "max_cod": 50000000,
        "supplier_description_vi_vn": "Đối tác nhận nhiều kiện hàng từ kho GHN và giao trong vòng 8 tiếng",
        "supplier_description_url": "https://ahamove.com/quy-trinh-hub-tmdt/",
        "opening_hours": "5-20",
        "max_cod_per_stop_point": 2000000,
        "vat_rate": 0.1,
        "available_districts": [
            "VN.HC.NB",
            "VN.HC.CG",
            "VN.HC.CC",
            "VN.HC.BC",
            "VN.HC.HM",
            "VN.BH",
            "VN.CM",
            "VN.LT",
            "VN.TDM",
            "VN.PG",
            "VN.TA",
            "VN.BC",
            "VN.BB",
            "VN.LK",
            "VN.XL",
            "VN.TP",
            "VN.VC",
            "VN.VT.TT",
            "VN.VT.XM",
            "VN.VT.DD",
            "VN.VT.VT",
            "VN.VT.BR",
            "VN.VT.CD",
            "VN.VT.CD",
            "VN.VT.LD",
            "VN.DA",
            "VN.HC.QB",
            "VN.HC.QC",
            "VN.HC.QG",
            "VN.HC.BH",
            "VN.HC.GV",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.PN",
            "VN.HC.QJ",
            "VN.HC.QD",
            "VN.HC.BT",
            "VN.HC.QF",
            "VN.HC.QA",
            "VN.HC.QE",
            "VN.HC.TB",
            "VN.HC.TD",
            "VN.HC.QH",
            "VN.HC.QI",
            "VN.HC.TP"
        ],
        "drop_off_districts": [
            "VN.HC.NB",
            "VN.HC.CG",
            "VN.HC.CC",
            "VN.HC.BC",
            "VN.HC.HM",
            "VN.BH",
            "VN.CM",
            "VN.LT",
            "VN.TDM",
            "VN.PG",
            "VN.TA",
            "VN.BC",
            "VN.BB",
            "VN.LK",
            "VN.XL",
            "VN.TP",
            "VN.VC",
            "VN.VT.TT",
            "VN.VT.XM",
            "VN.VT.DD",
            "VN.VT.VT",
            "VN.VT.BR",
            "VN.VT.CD",
            "VN.VT.CD",
            "VN.VT.LD",
            "VN.DA",
            "VN.HC.QB",
            "VN.HC.QC",
            "VN.HC.QG",
            "VN.HC.BH",
            "VN.HC.GV",
            "VN.HC.QK",
            "VN.HC.QL",
            "VN.HC.PN",
            "VN.HC.QJ",
            "VN.HC.QD",
            "VN.HC.BT",
            "VN.HC.QF",
            "VN.HC.QA",
            "VN.HC.QE",
            "VN.HC.TB",
            "VN.HC.TD",
            "VN.HC.QH",
            "VN.HC.QI",
            "VN.HC.TP"
        ],
        "priority_score": 6,
        "distance_fee_v3": {
            "blocks": [
                {
                    "from": 0,
                    "to": 100000,
                    "base": 0,
                    "price_multiplier": 0
                }
            ],
            "hour_rates": []
        },
        "group_id": "HUB-SP",
        "animated_url": "https://i.imgur.com/xiDxEYN.png",
        "requests": [
            {
                "_id": "SGN-HUB-SP-TRANSFER-COD",
                "name": "Thu hộ COD",
                "enable": True,
                "name_vi_vn": "Thu hộ COD",
                "name_en_us": "Collect COD",
                "icon_url": "https://s3-ap-southeast-1.amazonaws.com/ahamoveimg/core_services/ic_d2d.png",
                "order": 1,
                "no_commission": True,
                "price": 0,
                "type": "BOOLEAN",
                "description": "",
                "service_id": "SGN-HUB-SP",
                "transfer_cod": True,
                "service_group_id": "HUB-SP",
                "group_id": "TRANSFER_COD"
            }
        ],
        "currency": "VND"
    }
]

res = []

for elem in data:
    res.append(elem['name_vi_vn'])

res = '", "'.join(res)

print(res)
