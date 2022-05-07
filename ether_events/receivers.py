import json

from django_ethereum_events.chainevents import AbstractEventReceiver

from real_estate_backend.token_settings import decimals, image_bucket_info, image_bucket, meta_data_bucket, image_tmp_bucket
# from ether_events.models import Income
from token_info.models import RealEstateBaseInfo


class IncomeReceiver(AbstractEventReceiver):
    def save(self, decoded_event):
        pass
        # holder_ = decoded_event.args.holder
        # id_ = decoded_event.args.id
        # value_ = decoded_event.args.value
        # Income(holder=holder_, token_id=id_, value=value_).save()
        

class TransferSingleReceiver(AbstractEventReceiver):
    def save(self, decoded_event):
        from_ = getattr(decoded_event.args, "from")
        to_ = getattr(decoded_event.args, "to")
        id_ = getattr(decoded_event.args, "id")

        if from_ == "0x0000000000000000000000000000000000000000":
            filename = "%064X" % id_

            try:
                real_estateBase_info = RealEstateBaseInfo.objects.get(creator=to_)

                image = image_tmp_bucket.get_object("%d.jpg" % real_estateBase_info.id)
                image_bucket.put_object("%s.jpg" % filename, image)
            except Exception as e:
                name = str()
                description = str()
                img_url = str()
            else:
                name = real_estateBase_info.name
                description = real_estateBase_info.description
                img_url = "http://%s.%s/%s.jpg" % (image_bucket_info.name, image_bucket_info.end_point, filename)
            finally:
                meta_data = {
                    "name": name,
                    "description": description,
                    "decimals": decimals,
                    "image": img_url,
                }            

                meta_data_bucket.put_object("%s.json" % filename, json.dumps(meta_data))
            